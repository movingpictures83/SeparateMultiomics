# SeparateMultiomics
# Language: Python
# Input: TXT
# Output: PREFIX
# Tested with: PluMA 1.1, Python 3.6
# Dependency: pandas==1.1.5

Separate abundance into groups

Input is a TXT file of keyword-value pairs (tab-delimited):

multiomics: Path to multiomics CSV
metadata: Path to metadata CSV

Output will be multiple group files, using the user-specified prefix
