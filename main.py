import click
import cv2
import numpy as np
import os
import pdb
from sklearn.cluster import KMeans

PADDING = 50
DEFAULT_WIDTH = 1200
DEFAULT_HEIGHT = 400

@click.command()
@click.option('--path', help='File path for file or dir of videos to be processed.')
@click.option('--width', default=DEFAULT_WIDTH, help='Width of desired output image')
@click.option('--height', default=DEFAULT_HEIGHT, help='Height of desired output image')
def process_query(path, width, height):
    if os.path.isfile(path):
        files = [path]
    else:
        files = [path + f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    for video in files:
        process_video(video, int(width), int(height))

def process_video(video_path, width, height):
    video = cv2.VideoCapture(video_path)
    total_frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(total_frame_count)
    if (not video.isOpened()):
        click.echo("Error processing video {}.".format(video_path))
        return

    frame_count = 0
    divisor = int(total_frame_count / (width - (PADDING * 2)))
    graph = np.full((height, width+100, 3), 255, dtype=np.uint8)
    while (video.isOpened()):
        frame_count += 1
        ret, frame = video.read()
        if frame_count % divisor != 0:
            continue
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

            colors = sorted([(fraction, color) for (fraction, color) in zip(hist, centroids)], key=lambda tup: tup[0], reverse=True)
            draw_y_0 = PADDING
            draw_x = int((frame_count / divisor) + PADDING)
            for (fraction, color) in colors:
                print(color, "{:0.2f}%".format(fraction* 100))
                draw_y_1 = draw_y_0 + (fraction * (height - (PADDING* 2)))
                cv2.rectangle(graph, (draw_x, int(draw_y_0)), (draw_x + 1, int(draw_y_1)),
                        color.astype("uint8").tolist(), -1)
                draw_y_0 = draw_y_1
            print("=================================================================")

        else:
            break

    graph = cv2.cvtColor(graph, cv2.COLOR_RGB2BGR)
    file_name = os.path.splitext(os.path.basename(video_path))[0]
    cv2.putText(graph, file_name, (PADDING, int(PADDING/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1)
    cv2.imwrite("processed_" + file_name + ".jpg", graph)
    video.release()

if __name__ == '__main__':
    process_query()
