
#*********************************************************************************#

# Biological parameters for VNTR simulation
# -----------------------------------------


# reference file from which to simulate reads from: reference_file - needs to be indexed
# VNTR coordinates: vntr_coordinates - can be read from a file (e.g. a BED file with the VNTR coordinates and motifs)
# VNTR motif: motif - need to decide if you want the user to input the motif or if it can be read from a file (e.g. a BED file with the VNTR coordinates and motifs)
# VNTR motif period: period - can be calculated from the motif length
# VNTR reference copy number: ref_copy_number
# VNTR gc%: gc_content - can be calculated from motif sequence x copy number
# VNTR genotype: genotype - either homozygous or heterozygous, if heterozygous then need to specify the copy number for each allele
# VNTR allele1 motif: allele1_motif - if heterozygous, need to specify the motif for each allele
# VNTR allele1 copy number: allele1_copy_number - if heterozygous, need to specify the copy number for each allele
# VNTR allele2 motif: allele2_motif - if heterozygous, need to specify the motif for each allele
# VNTR allele2 copy number: allele2_copy_number - if heterozygous, need to specify the copy number for each allele

#*********************************************************************************#

# Technical parameters for VNTR simulation
# ----------------------------------------

# number of reads to simulate: n_reads -calculated from the coverage formula
# whether paired-end or single-end reads: paired_end - boolean
# read length: read_length
# insert size (for paired-end reads): insert_size
# sequencing error rate: error_rate
# sequencing error profile: error_profile - can be a file with the error profile for the sequencing platform being simulated (e.g. Illumina, PacBio, Oxford Nanopore)
# sequencing platform: sequencing_platform - can be used to determine the error profile and error rate for the simulation

#*********************************************************************************#

# I/O parameters for VNTR simulation
# ----------------------------------

# genotype output file format: output format - BED or VCF, need to convert between genotyper output and desired output format if necessary
# output file name: output_file_name
# output file directory: output_file_directory
# whether to plot or not: plot - boolean
# what metric to use for evaluation: evaluation_metric - RMSE, repeat lengths, R between ground truth and simulated data
# where to output plots: plot_directory