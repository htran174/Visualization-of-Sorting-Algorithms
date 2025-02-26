import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def show_graph(dictionary):

    #all the selected sort
    categories = list(dictionary.keys())

    #all the sorted time
    values = list(dictionary.values())

    # Seaborn style
    sns.set_style("whitegrid")

    # Create figure and axis
    fig, ax = plt.subplots()
    bars = ax.bar(categories, [0] * len(values), color=sns.color_palette("husl", len(values)))

    # Set limits
    ax.set_ylim(0, max(values) + 2)
    ax.set_title("Sorted Time")

    # Number of frames
    frames = 30

    # Animation function
    def update(frame):
        progress = (frame + 1) / frames  # Normalize frame count to range [0, 1]
        for bar, target_value in zip(bars, values):
            bar.set_height(target_value * progress)  # Scale the height incrementally
        if frame == frames - 1:  # Stop animation when reaching the last frame
            ani.event_source.stop()

    # Create animation
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, repeat=False)


    # Show animation
    plt.show()
