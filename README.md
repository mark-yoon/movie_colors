# Movie colors
*A tool to analyze the color palettes used in movies.*  
Movie colors is a CLI tool to allow you to visualize the color palettes used in movies.

Using OpenCV, the script selects a regular number of frames from a given video. For each frame, the top three most prevelant colors are found using k-means clustering. These colors are then drawn on an output image sorted by most to least common.

### Usage
---

Params:  
```
--path                File path for file or dir of videos to be processed
--width               Width of desired output image
--height              Height of desired output image
--buckets             Number of top colors per frame
```

### Samples
---
#### Batman 1989
![](https://raw.githubusercontent.com/mark-yoon/movie_colors/master/samples/batman/processed_batman_1989.jpg)

#### Batman 1992
![](https://raw.githubusercontent.com/mark-yoon/movie_colors/master/samples/batman/processed_batman_1992.jpg)

#### Batman 1995
![](https://raw.githubusercontent.com/mark-yoon/movie_colors/master/samples/batman/processed_batman_1995.jpg)

#### Batman 2005
![](https://raw.githubusercontent.com/mark-yoon/movie_colors/master/samples/batman/processed_batman_2005.jpg)

#### Batman 2008
![](https://raw.githubusercontent.com/mark-yoon/movie_colors/master/samples/batman/processed_batman_2008.jpg)

#### Batman 2012
![](https://raw.githubusercontent.com/mark-yoon/movie_colors/master/samples/batman/processed_batman_2012.jpg)

#### Superman 1978
![](https://raw.githubusercontent.com/mark-yoon/movie_colors/master/samples/superman/processed_superman_1978.jpg)

#### Superman 1980
![](https://raw.githubusercontent.com/mark-yoon/movie_colors/master/samples/superman/processed_superman_1980.jpg)

#### Superman 1983
![](https://raw.githubusercontent.com/mark-yoon/movie_colors/master/samples/superman/processed_superman_1983.jpg)

#### Superman 1987
![](https://raw.githubusercontent.com/mark-yoon/movie_colors/master/samples/superman/processed_superman_1987.jpg)

#### Superman 2006
![](https://raw.githubusercontent.com/mark-yoon/movie_colors/master/samples/superman/processed_superman_2006.jpg)

#### Superman 2013
![](https://raw.githubusercontent.com/mark-yoon/movie_colors/master/samples/superman/processed_superman_2013.jpg)
