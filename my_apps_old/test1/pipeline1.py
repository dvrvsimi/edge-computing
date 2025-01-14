#!/usr/bin/env python3
import sys

import gi

gi.require_version('GLib', '2.0')
gi.require_version('GObject', '2.0')
gi.require_version('Gst', '1.0')

from gi.repository import Gst, GObject, GLib

pipeline = None
bus = None
message = None

# initialize GStreamer
Gst.init(sys.argv[1:])

# build the pipeline
pipeline = Gst.parse_launch(
     "playbin uri=file:///home/hlk/Documents/ai6/edge-computing/my_apps/sample_stream/sample_1080p_h265.mp4"
)

# start playing
pipeline.set_state(Gst.State.PLAYING)

# wait until EOS or error
bus = pipeline.get_bus()
msg = bus.timed_pop_filtered(
    Gst.CLOCK_TIME_NONE,
    Gst.MessageType.ERROR | Gst.MessageType.EOS
)

# free resources
pipeline.set_state(Gst.State.NULL)


# /dli/task/deepstream/samples/streams/yoga.mp4
# https://www.freedesktop.org/software/gstreamer-sdk/data/media/sintel_trailer-480p.webm