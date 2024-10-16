import io
import matplotlib
import matplotlib.pyplot as plt
import hyperdiv as hd

matplotlib.use("Agg")


def get_chart_image(fig):
    """
    Renders the chart to png image bytes.
    """
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    image_bytes = buf.getvalue()
    buf.close()
    plt.close(fig)
    return image_bytes


def main():
    # Create a chart:
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [10, 11, 12, 13])

    # Render the image bytes in the UI:
    hd.image(get_chart_image(fig), width=20)


hd.run(main)
