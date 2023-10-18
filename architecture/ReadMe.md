::: mermaid
classDiagram
    class integration {
    class camera
    class image_visualizer
    class image_processor
    class data_logger
    run()
  }
  class camera {
    frame
    cap
    __init__(,camera_index)
    get_frame()
    camera_open()
    camera_close()
  }

  class image_visualizer {
    frame_show
    draw_frame()
    draw_label()
    show_frame()
  }

  class image_processor {
    image
    shapes_and_colors
    gray_image
    binary_image
    edges
    contours
    convert_to_grayscale()
    picture_binary()
    find_edges()
    find_contours()
    shape_detection()
    color_detection()
  }

  class data_logger {
    csv_data
    timestamp()
    csv_save()
  }

  integration --|>  camera
  integration --|>  image_visualizer
  integration --|>  image_processor
  integration --|>  data_logger
  image_visualizer --|> image_processor


:::


::: mermaid
sequenceDiagram
participant i as _init_
participant co as camera_open()
participant gf as get_frame()
participant cc as camera_close()

i -->> co: index
co -->> co: open camera
gf -->> gf: get as many frames you want
cc -->> cc: close cam in the end
:::

::: mermaid
sequenceDiagram
participant i as _init_
participant ctg as convert_to_grayscale()
participant pb as picture_binary()
participant fe as find_edges()
participant fc as find_contours()
participant sd as shape_detection()
participant cd as color_detection()

i -->> ctg: image
ctg -->> pb: grey_image
pb -->> fe: binary_image
fe -->> fc: edges
fc -->> sd: contours
sd -->> cd: shapes_and_colors
:::

::: mermaid
sequenceDiagram
participant i as _init_
participant df as draw_frame()
participant dl as draw_label()
participant sf as show_frame()

i -->> df: contours
i -->> dl: contours and label
df -->> sf: frame
dl -->> sf: shapes_and_colors

:::

::: mermaid
sequenceDiagram
participant i as _init_
participant ts as timestamp()
participant cs as csv_save()
i --> cs: shape and color
ts -->> cs: date

:::

::: mermaid
sequenceDiagram
participant r as run()
participant c as class::camera
participant ip as class::image_processor
participant iv as class::image_visualizer
participant dl as class::data_logger

r --> c: index camera
c -->> ip: image
ip --> iv: shapes and color data
ip -->> dl: shapes and color data
r -->> c: if q pressed close cam and break

:::
