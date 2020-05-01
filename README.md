## Movie colors
*A tool to analyze the color palettes used in movies.*
Movie colors is a CLI tool to allow you to visualize the color palettes used in movies.

Using OpenCV, the script selects a regular number of frames from a given video. For each frame, the top three most prevelant colors are found using k-means clustering. These colors are then drawn on an output image sorted by most to least common.

Some samples of these images can be found in `samples/`.

### Usage

Params:  
```
--path                File path for file or dir of videos to be processed
--width               Width of desired output image
--height              Height of desired output image
--buckets             Number of top colors per frame
```
