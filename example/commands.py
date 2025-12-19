import itertools
import os
import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument('sample_list_file', type=click.File('r'))
@click.argument('output_pair_file', type=click.File('w'))
def make_pairs(sample_list_file, output_pair_file):
    sample_list = [sample.strip() for sample in sample_list_file]
    for pair in itertools.combinations(sample_list, 2):
        line = "\t".join(pair) + '\n'
        output_pair_file.write(line)


@cli.command()
@click.argument('sample_list_file', type=click.File('r'))
@click.argument('sample_input_file', type=click.File('w'))
@click.argument('sample_data_dir')
@click.option('-p', '--use_peaks', default=False, type=bool, deprecated=True)
@click.option('-b', '--use_bedpe', default=False, type=bool) # Default is False i.e. default to Hi-C format
def make_sample_input_file(sample_list_file, sample_input_file, sample_data_dir, use_peaks, use_bedpe):
    bg_ext = '.bedgraph'
    bw_ext = '.bw'
    if use_bedpe:
        hic_ext = '.bedpe'
    else:
        hic_ext = '.hic'
    peak_ext = '.bed'

    for sample_name in sample_list_file:
        sample_name = sample_name.strip()

        # Get file paths for each needed file
        bg_file_path = None
        hic_file_path = None
        peak_file_path = None
        for file in os.scandir(sample_data_dir):
            if (file.name.lower().endswith(bg_ext) or file.name.lower().endswith(bw_ext)) and sample_name.lower() in file.name.lower():
                bg_file_path = file.path
            elif (file.name.lower().endswith(hic_ext)) and sample_name.lower() in file.name.lower():
                hic_file_path = file.path
            elif use_peaks and file.name.lower().endswith(peak_ext) and sample_name.lower() in file.name.lower():
                peak_file_path = file.path

        if not bg_file_path or not hic_file_path:
            print(f'Missing files for {sample_name}. Skipping.')
            continue

        if use_peaks and not peak_file_path:
            print(f'Missing peak file for {sample_name} but use_peaks is True. Skipping.')
            continue

        if use_peaks:
            sample_input_file.write(f'{sample_name}\t{bg_file_path}\t{hic_file_path}\t{peak_file_path}\n')
            # A difference from the original program is that the last column is the peak
            # The oriignal code had it as the second to last column
        else:
            sample_input_file.write(f'{sample_name}\t{bg_file_path}\t{hic_file_path}\n')


if __name__ == '__main__':
    cli()
