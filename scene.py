import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    # 
    """   tree_center = scene_left + 500
    tree_top = scene_top + 100
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)"""
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    screenx0 = scene_left 
    screeny0 = scene_bottom - 50
    screenx1 = scene_right + 600
    screeny1 = scene_top
    draw_sky(canvas,screenx0,screeny0,screenx1,screeny1)
    draw_ground(canvas,scene_left,scene_bottom,scene_right,scene_top)
    draw_cloud(canvas,scene_left,scene_bottom,scene_right,scene_top)
    draw_tree(canvas,scene_left,scene_bottom,scene_right,scene_top)
# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_sky(canvas,x0,y0,x1,y1,):
    canvas.create_rectangle(x0,y0,x1,y1,outline="black",fill="blue")



def draw_ground(canvas,scene_left,scene_bottom,scene_right,scene_top):
    canvas.create_rectangle(scene_left,scene_bottom + 600,scene_right + 600,scene_top + 450,outline="black",fill="sienna1")


def draw_cloud(canvas,scene_left,scene_bottom,scene_right,scene_top):
        canvas.create_oval(scene_right -300 ,scene_top  ,scene_left ,scene_bottom - 400 ,fill="white")
        canvas.create_oval(scene_right + 100  ,scene_top + 30 ,scene_left + 100 ,scene_bottom - 370 ,fill="white")
        canvas.create_oval(scene_right + 150  ,scene_top ,scene_left +150 ,scene_bottom - 430 ,fill="white")
        canvas.create_oval(scene_right  ,scene_top ,scene_left + 100 ,scene_bottom - 400 ,fill="white")
        canvas.create_oval(scene_right - 300  ,scene_top ,scene_left - 300 ,scene_bottom - 400 ,fill="white")
        canvas.create_oval(scene_right + 550 ,scene_top ,scene_left + 1200 ,scene_bottom - 350 ,fill="yellow")

def draw_tree(canvas,x0,y0,x1,y1):
       canvas.create_polygon(x0 + 300 , y0 +100 , x1 - 300 , y1 + 600, 400 ,200,fill="dark green")
       canvas.create_polygon(x0 + 400 , y0 +200 , x1 - 400 , y1 + 500, 400 ,200,fill="black")
       canvas.create_rectangle(x0 + 370 ,y0 + 300,x1 - 370,y1 + 600,outline="brown",fill="saddleBrown")




"""def draw_pine_tree(canvas, peak_x, peak_y, height):"""
"""Draw a single pine tree  Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
"""
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")
"""

# Call the main function so that
# this program will start executing.
main()