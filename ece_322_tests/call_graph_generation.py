from pycallgraph import PyCallGraph, Config
from pycallgraph.output import GraphvizOutput

import pendulum

config = Config()
config.include_stdlib = True
config.debug = True
config.verbose = True


output_parse = GraphvizOutput()
output_parse.output_file = "pendulum_parse_call_graph.png"
with PyCallGraph(output=output_parse, config=config):
    date = pendulum.parse("2018-01-01")


output_parse = GraphvizOutput()
output_parse.output_file = "pendulum_parse_bad_call_graph.png"
with PyCallGraph(output=output_parse, config=config):
    try:
        date = pendulum.parse("15512-412")
    except Exception:
        pass


output_parse = GraphvizOutput()
output_parse.output_file = "pendulum_parse_strict_bad_call_graph.png"
with PyCallGraph(output=output_parse, config=config):
    try:
        date = pendulum.parse("18-01-01", strict=True)
    except Exception:
        pass


output_parse = GraphvizOutput()
output_parse.output_file = "pendulum_parse_strict_false_call_graph.png"
with PyCallGraph(output=output_parse, config=config):
    date = pendulum.parse("18-01-01", strict=False)


output_now = GraphvizOutput()
output_now.output_file = "pendulum_now_call_graph.png"
with PyCallGraph(output=output_now, config=config):
    date = pendulum.now()


output_duration = GraphvizOutput()
output_duration.output_file = "pendulum_duration_simple_call_graph.png"
with PyCallGraph(output=output_duration, config=config):
    date = pendulum.duration()


output_duration = GraphvizOutput()
output_duration.output_file = "pendulum_duration_adv_call_graph.png"
with PyCallGraph(output=output_duration, config=config):
    date = pendulum.duration(days=5)
