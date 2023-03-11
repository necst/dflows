from typing import Union

from dovado_rtl.explorers.tasks import (
    AutomaticExplorationProject,
    ManualExplorationProject,
    Probe,
)
from dovado_rtl.input import Input
from dovado_rtl.parsers.parse import parse as general_parse
from dovado_rtl.parsers.verilog.verilog_parser import VerilogParser


def parse(
    input_project: Input,
) -> Union[AutomaticExplorationProject, ManualExplorationProject, Probe]:
    return general_parse(input_project, VerilogParser)
