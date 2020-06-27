"""Unit tests for the multi rename library."""

from multi_rename import renamer
import os
import shutil


class TestRenamer:

    def test_prefix(self):
        test_file_dir = os.path.join(os.getcwd(), 'tests', 'data')
        src_test_data = os.path.join(os.getcwd(), 'tests', 'src_data')

        test_renamed_files = []
        for filename in os.listdir(test_file_dir):
            if not os.path.isdir(os.path.join(test_file_dir, filename)):
                test_renamed_files.append('pre_' + filename)

        renamed_files = renamer.add_affix(
            dir_path=test_file_dir, affix_type='prefix', affix='pre', sep='_')

        shutil.rmtree(test_file_dir)
        shutil.copytree(src_test_data, test_file_dir)

        assert sorted(test_renamed_files) == sorted(renamed_files)

    def test_suffix(self):
        test_file_dir = os.path.join(os.getcwd(), 'tests', 'data')
        src_test_data = os.path.join(os.getcwd(), 'tests', 'src_data')

        test_renamed_files = []
        for filename in os.listdir(test_file_dir):
            if not os.path.isdir(os.path.join(test_file_dir, filename)):
                name, ext = os.path.splitext(filename)
                test_renamed_files.append(name + '_suff' + ext)

        renamed_files = renamer.add_affix(
            dir_path=test_file_dir, affix_type='suffix', affix='suff', sep='_')

        shutil.rmtree(test_file_dir)
        shutil.copytree(src_test_data, test_file_dir)

        assert sorted(test_renamed_files) == sorted(renamed_files)

    def test_full_rename(self):
        test_file_dir = os.path.join(os.getcwd(), 'tests', 'data')
        src_test_data = os.path.join(os.getcwd(), 'tests', 'src_data')

        filenames = os.listdir(test_file_dir)
        idx = 1

        test_renamed_files = []
        for filename in filenames:
            if not os.path.isdir(os.path.join(test_file_dir, filename)):
                extension = os.path.splitext(filename)[1]
                if extension[1:] != 'html':
                    test_renamed_files.append(
                        'newsample_' + str(idx) + extension)
                    idx += 1

        renamed_files = renamer.full_rename(
            dir_path=test_file_dir, new_name='newsample', sep='_', filter_ext='html')

        shutil.rmtree(test_file_dir)
        shutil.copytree(src_test_data, test_file_dir)

        assert sorted(test_renamed_files) == sorted(renamed_files)
