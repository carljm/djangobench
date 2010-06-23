from djangobench.utils import run_benchmark
from query_complex_filter.models import Book

def benchmark():
    Book.objects.complex_filter({'pk': 1})

run_benchmark(
    benchmark,
    meta = {
        'description': 'A simple Model.objects.complex_filter() call.',
    }
)
