# Biological Computation Task 1


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r /path/to/requirements.txt
```

## Usage

```python
import sub_graphs_calculator as sub

# returns all weakly connected sub-graphs of size k
sub_graphs = sub.generate_all_graphs_of_size_k(4)

# writes to file size_4_sub_graphs.txt all sub-graphs of size k(4)
sub.write_all_graphs(sub_graphs,4,"size_4_sub_graphs.txt")

```
## Contributing
Ziv Assoulin,Noam

