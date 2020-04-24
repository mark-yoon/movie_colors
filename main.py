import click
import cv2
import numpy as np
import os
from sklearn.cluster import KMeans

@click.command()
@click.option('--video', help='File path for video to be processed.')
@click.option('--videos', help='File directory for video to be processed.')
@click.option('--dest', default='./', help='Directory location to save processed video.')
def process_query(video, videos, dest):
    if (video):
        videos = [video]

    for video in videos:
        process_video(video)

def process_video(video_path):
    video = cv2.VideoCapture(video_path)
    if (not video.isOpened()):
        click.echo("Error processing video {}.".format(video_path))
        return

    frame_count = 0
    graph = np.zeros((1000, 1000, 3), dtype=np.uint8)
    while (video.isOpened()):
        frame_count += 1
        ret, frame = video.read()
        if ret:
            click.echo("Processing frame #{}".format(frame_count))
            # change colorspace
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # reshape frame
            frame = frame.reshape((frame.shape[0] * frame.shape[1], 3))
            # get clusters and centroids
            cluster = KMeans(n_clusters=5).fit(frame)
            centroids = cluster.cluster_centers_

            labels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
            hist, _ = np.histogram(cluster.labels_, bins = labels)
            hist = hist.astype("float")
            hist = hist / hist.sum()

            colors = sorted([(fraction, color) for (fraction, color) in zip(hist, centroids)], reverse=True)
            start = 0
            for (fraction, color) in colors:
                print(color, "{:0.2f}%".format(fraction* 100))
                end = start + (fraction * 1000)
                cv2.rectangle(graph, (int(start), frame_count), (int(end), frame_count + 2),
                        color.astype("uint8").tolist(), -1)
                start = end
            print("=================================================================")

        else:
            break

    graph = cv2.cvtColor(graph, cv2.COLOR_RGB2BGR)
    cv2.imshow('Color graph', graph)
    cv2.waitKey()
    video.release()

if __name__ == '__main__':
    process_query()
