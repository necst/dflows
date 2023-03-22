import os
from pathlib import Path
from pydantic import ValidationError
import pytest
import toml

from dovado_rtl.input import Input


def test_input():
    path_prefix: str = "resources/configs"

    to_parse = Path(path_prefix + "/test_config.toml")
    input_data = Input.make_from_file(to_parse)

    assert isinstance(input_data, Input)
    assert input_data.board == "some_board_name"
    assert input_data.project_root == Path("resources/neorv32/rtl")

    assert input_data.target_file == Path("core/neorv32_top.vhd")
    assert input_data.task_file == Path(
        "resources/exploration_files/neorv_exploration_file.csv"
    )
    assert input_data.target_module == "neorv32_top"
    assert input_data.clock_port == "clk_i"

    assert input_data.synthesis_directives == ["RuntimeOptimized"]
    assert input_data.implementation_directives == ["RuntimeOptimized"]
    assert input_data.default_metrics == ["lut_occupation", "frequency"]
    assert list(input_data.custom_metrics.keys()) == [
        "test_metric",
        "another_test_metric",
    ]

    to_parse = Path(path_prefix + "/broken_test_config.toml")
    with pytest.raises(ValueError):
        input_data = Input.make_from_file(to_parse)
