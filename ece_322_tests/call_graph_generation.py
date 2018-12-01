from pycallgraph import PyCallGraph, Config
from pycallgraph.output import GraphvizOutput

import pendulum

config = Config()
config.include_stdlib = True
config.debug = True
config.verbose = True


output = GraphvizOutput()
output.output_file = "pendulum_parse_call_graph.png"
output.output_type = "png"
with PyCallGraph(output=output, config=config):
    date = pendulum.parse("2018-01-01")


output = GraphvizOutput()
output.output_file = "pendulum_parse_bad_call_graph.png"
output.output_type = "png"
with PyCallGraph(output=output, config=config):
    try:
        date = pendulum.parse("15512-412")
    except Exception:
        pass


output = GraphvizOutput()
output.output_file = "pendulum_parse_strict_bad_call_graph.png"
output.output_type = "png"
with PyCallGraph(output=output, config=config):
    try:
        date = pendulum.parse("18-01-01", strict=True)
    except Exception:
        pass


output = GraphvizOutput()
output.output_file = "pendulum_parse_strict_false_call_graph.png"
output.output_type = "png"
with PyCallGraph(output=output, config=config):
    date = pendulum.parse("18-01-01", strict=False)


output = GraphvizOutput()
output.output_file = "pendulum_now_call_graph.png"
output.output_type = "png"
with PyCallGraph(output=output, config=config):
    date = pendulum.now()


output = GraphvizOutput()
output.output_file = "pendulum_duration_simple_call_graph.png"
output.output_type = "png"
with PyCallGraph(output=output, config=config):
    date = pendulum.duration()


output = GraphvizOutput()
output.output_file = "pendulum_duration_in_words_call_graph.png"
output.output_type = "png"
with PyCallGraph(output=output, config=config):
    dur = pendulum.duration()
    dur.in_words()

