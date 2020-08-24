coverage erase
coverage run --branch --parallel-mode ../examples/example.py -l -a "GPIB0::8::INSTR"
coverage combine
coverage report
coverage html
