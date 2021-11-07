"""auto_cracks_dataset dataset."""

import tensorflow as tf
import tensorflow_datasets as tfds
import json
import os

# TODO(auto_cracks_dataset): Markdown description  that will appear on the catalog page.
_DESCRIPTION = """
Description is **formatted** as markdown.

It should also contain any processing which has been applied (if any),
(e.g. corrupted example skipped, images cropped,...):
"""

# TODO(auto_cracks_dataset): BibTeX citation
_CITATION = """
"""
_NAMES= ['Repair', 'Replacement']


class AutoCracksDataset(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for auto_cracks_dataset dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    # TODO(auto_cracks_dataset): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            'image': tfds.features.Image(shape=(224, 224, 3)),
            'label': tfds.features.ClassLabel(names=_NAMES),
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=('image', 'label'),  # Set to `None` to disable
        homepage='https://dataset-homepage/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # TODO(auto_cracks_dataset): Downloads the data and defines the splits
   #path = dl_manager.download_and_extract('https://todo-data-url')
    path =  os.getcwd()+os.path.normpath('/damages_dataset_224_cropped/')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(path)
    # TODO(my_dataset): Returns the Dict[split names, Iterator[Key, Example]]
    return {
        'train': self._generate_examples(path),
    }

  def _generate_examples(self, path):
    meta = open(os.path.join(path,'dataset_metadata.json'))
    jsn = json.load(meta)
    print('\n\n\n',type(jsn), '\n\n\n')
    for record in jsn:
      image_path = path+os.path.join(os.path.normpath('/train/'), record['label'] ,os.path.normpath(record['fileName']))
      print(image_path)
      yield record['fileName'], {
          'image': image_path,
          'label': record['label'].capitalize()
      }
