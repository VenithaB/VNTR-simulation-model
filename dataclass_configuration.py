
#*********************************************************************************#

# Biological parameters for VNTR simulation
# -----------------------------------------


# reference file from which to simulate reads from: reference_file - needs to be indexed
# chromosome: chromosome
# VNTR start position: start_position
# VNTR end position: end_position
# VNTR motif: motif - need to decide if you want the user to input the motif or if it can be read from a file (e.g. a BED file with the VNTR coordinates and motifs)
# VNTR reference copy number: ref_copy_number
# VNTR allele1 motif: allele1_motif - if heterozygous, need to specify the motif for each allele
# VNTR allele1 copy number: allele1_copy_number - if heterozygous, need to specify the copy number for each allele
# VNTR allele2 motif: allele2_motif - if heterozygous, need to specify the motif for each allele
# VNTR allele2 copy number: allele2_copy_number - if heterozygous, need to specify the copy number for each allele

#*********************************************************************************#

# Technical parameters for VNTR simulation
# ----------------------------------------

# seed for reproducibility: seed
# coverage: coverage
# whether paired-end or single-end reads: paired_end - boolean
# read length: read_length
# insert size (for paired-end reads): insert_size
# sequencing error rate: error_rate
# genotyper: Either 'adVNTR', 'VNTRseek' or 'danbing-tk'

#*********************************************************************************#

# I/O parameters for VNTR simulation
# ----------------------------------

# run name: run_name
# output file directory: output_file_directory

from dataclasses import dataclass, field

@dataclass
class configuration:
    # Fields with no default values first
    #------------------------------------
    # Biological fields
    path_to_reference_genome: str
    # need to figure out if I need a separate config class for each genotyper, coz some take BED files, some take a DB
    chromosome: str
    vntr_reference_start: int
    vntr_reference_end: int
    vntr_reference_motif: str
    vntr_reference_copy_number: int

    vntr_allele1_motif: str
    vntr_allele1_copy_number: int
    vntr_allele2_motif: str
    vntr_allele2_copy_number: int

    # Technical fields
    seed: int
    coverage: int

    # I/O fields
    run_name: str

    #------------------------------------
    # Default fields
    #------------------------------------
    read_length: int = 150
    paired_end: bool = True
    insert_size: int = 300
    error_rate: float = 0.01
    genotyper: list[str] = field(default_factory=lambda: ["adVNTR", "VNTRseek", "danbing-tk"])
    output_file_directory: str = "."

    # Test