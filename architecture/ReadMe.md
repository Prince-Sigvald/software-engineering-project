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


:::

::: mermaid
sequenceDiagram

  participant r as run()
  participant ci as cam __init__
  participant co as camera_open()
  participant cc as camera_close()
  participant gf as get_frame()
  participant df as draw_frame()
  participant dl as draw_label()
  participant sf as show_frame()
  participant iip as img_proc___init__
  participant ctg as convert_to_grayscale()
  participant pb as picture_binary()
  participant fe as find_edges()
  participant fc as find_contours()
  participant sd as shape_detection()
  participant cd as color_detection()
  participant ts as timestamp()
  participant cs as csv_save()


  r --> ci: choose camera
  r -->> co: open camera
  gf -->> r: frame
  r -->> ctg: frame
  ctg -->> pb: grey_image
  pb -->> fe: binary_image
  fe -->> fc: edges
  fc -->> sd: contours
  sd -->> cd: shapes_and_colors
  cd -->> r: shapes_and_colors
  r -->> cs: shapes_and_colors
  ts -->> cs: data
  r -->> df: contours
  r -->> df: frame
  r -->> dl: shapes_and_colors
  dl -->> sf: frame_show
  



:::