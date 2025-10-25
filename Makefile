setup:
\tpython -m pip install --upgrade pip
\tpip install -e .
\tpip install pytest ruff mypy

run:
\tfml run --steps 200000 --seed 123 --save-media ./media

test:
\tpytest -q

lint:
\truff check .
\tmypy fml
