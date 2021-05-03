
# COREugate - A pipeline for cgMLST
## From contigs to cgMLST profile and SLC.

COREugate has had a small facelift!! Under the hood we are now using [NextFlow](https://www.nextflow.io) as our pipeline engine and have introduced some additional functionality for clustering the profiles.

1. PrepSchema (if necessary) and Call alleles using [chewBBACA](https://github.com/B-UMMI/chewBBACA/wiki).
2. Combine profiles and statisitics for the whole dataset.
3. Calculate pairwise allelic distances (missing data is ignored)
4. Perform SLC to group related profiles, based on user supplied thresholds.

### Dependencies
```
Python >=3.7
Biopython >=1.70
Nextflow >=20.10
chewBBACA >=2.6
```

### NextFlow
Ensure that you have NextFlow installed. Detailed instructions can be found [here](https://www.nextflow.io/docs/latest/getstarted.html#installation)

### chewBBACA
[chewBBACA](https://github.com/B-UMMI/chewBBACA/) is used here to prepare the schema, by selecting exemplar alleles for comparison and to call allele profiles. More information about chewBBACA and how it is works can be found [here](https://github.com/B-UMMI/chewBBACA/wiki). COREugate can use a singularity version of chewBBACA, however if you want to install the latest version (>=2.0.16)

### Run COREugate

#### Get COREugate
```
pip3 install git+https://github.com/kristyhoran/Coreugate
```

If you are installing COREugate on a server using `--user` please ensure that your `~/.local/bin` is part of your PATH
```
export PATH=$PATH:/path/to/.local/bin
```

#### Running COREugate

```
coreugate [-h] [-v] [--input_file INPUT_FILE]
                 [--schema_path SCHEMA_PATH]
                 [--prodigal_training PRODIGAL_TRAINING] [--workdir WORKDIR]
                 [--threads THREADS]
                 [--filter_samples_threshold FILTER_SAMPLES_THRESHOLD]
                 [--cluster] [--cluster_thresholds CLUSTER_THRESHOLDS]
                 [--force] [--report]

Coreugate - a cgMLST pipeline implementing chewBACCA

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --input_file INPUT_FILE, -i INPUT_FILE
                        Input file tab-delimited file3 columns isolate_id
                        path_to_input_file (contigs) (default: )
  --schema_path SCHEMA_PATH, -s SCHEMA_PATH
                        Path to species schema/allele db (or url if using
                        chewie Nomenclature server) (default: )
  --prodigal_training PRODIGAL_TRAINING, -p PRODIGAL_TRAINING
                        Prodigal file to be used in allele calling. See https:
                        //github.com/B-UMMI/chewBBACA/tree/master/CHEWBBACA/pr
                        odigal_training_files for options (default: )
  --workdir WORKDIR, -w WORKDIR
                        Working directory, default is current directory
                        (default: /home/khhor/validation/salmonella_typing/rev
                        erification_20210322)
  --threads THREADS, -t THREADS
                        Number of threads to run chewBACCA (default: 16)
  --filter_samples_threshold FILTER_SAMPLES_THRESHOLD, -ft FILTER_SAMPLES_THRESHOLD
                        The proportion of loci present in a sample for an
                        sample to be included in further analysis (0-1)
                        (default: 0.95)
  --cluster, -c         If you would like to cluster the pairwise distance
                        matrix. If selected you must provide a list of
                        thresholds. (default: False)
  --cluster_thresholds CLUSTER_THRESHOLDS, -ct CLUSTER_THRESHOLDS
                        Provide a comma separate list (NO SPACES) eg 20,40,200
                        (default: )
  --force, -f           If you want to force chewBBACA to re-run. (default:
                        False)
  --report              Save nextflow reports. (default: False)
                                 Display this help message
```


###### Sample data

*Assemblies*
```
isolate_name	path/to/assembly.fa	
```
###### Species cgMLST schema
COREugate requires an exisiting cgMLST schema, this can be a schema generated by the user or downloaded from one of the publically available databases. These schema should be in the format of a `fasta` file for each loci, each file should contain the different alleles for each loci. It should be noted that during allele calling, chewBBACA (implemented by COREugate) will add inferred alleles ([more information](https://github.com/B-UMMI/chewBBACA/wiki)) to your schema, so it is recommended that the schema path be fixed, that is that the schema is kept in a central location and a single version is used for each species/study.

###### Other optional arguments
* `prodigal_training` a prodigal training file for allele calling. Recommended by chewBBACA developers, a list of default training files and further information can be found [here](https://github.com/B-UMMI/chewBBACA/wiki).


### Limitations of the pipeline
* Coreugate is only able to work with pre-exisiting schemas that have been prep as described above, to derive profiles for isolates.
* Possibly more, I just haven't found them yet!!

