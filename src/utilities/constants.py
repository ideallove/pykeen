# -*- coding: utf-8 -*-
# Basic Directory
from utilities.config_utils import create_base_dir

KG_EMBEDDINGS_PIPELINE_DIR = create_base_dir()

# Related to corpus Walking RDF and OWL
WROC = 'walking_rdf_and_owl_corpus'
WROC_URL = 'http://aber-owl.net/aber-owl/bio2vec/bio-knowledge-graph.n3'

# WN18 related
WN18_URL = 'https://github.com/Mrlyk423/Relation_Extraction/raw/master/data.zip'
WN_18 = 'wn_18'
WN_18_TRAIN = 'train'
WN_18_VALID = 'valid'
WN_18_TEST = 'test'


# Related to CSQA filtered Wikidata
CSQA_WIKIDATA = 'csqa_wiki_data'

# Configuration related
CLASS_NAME = 'class_name'
## Reader
READER = 'reader'
WROC_READER = 'WROCReader'
CSQA_WIKIDATA_READER = 'CSQAWikiDataReader'
WN18_READER = 'WN18Reader'
## KG embedding model
KG_EMBEDDING_MODEL = 'kg_embedding_model'
TRANS_E = 'TransE'
TRANS_H = 'TransH'
# Evaluator
EVALUATOR = 'evaluator'
MEAN_RANK_EVALUATOR = 'MeanRankEvaluator'
# Output paths
ENTITY_TO_EMBEDDINGS = 'entity_to_embeddings'
EVAL_RESULTS ='eval_results'
# Device related
PREFERRED_DEVICE  = 'preferred_device'
CPU = 'cpu'
GPU = 'gpu'
# Hyperparamters optim
HPO = 'hyper_param_optimization'
RANDOM_SEARCH_OPTIMIZER = 'random_search_optimizer'

## Metrics
MEAN_RANK = 'mean_rank'
HITS_AT_K = 'hits@k'
# ML params
BATCH_SIZE = 'batch_size'
VOCAB_SIZE = 'vocab_size'
EMBEDDING_DIM = 'embedding_dim'
MARGIN_LOSS = 'margin_loss'
NUM_ENTITIES = 'num_entities'
NUM_RELATIONS = 'num_relations'
NUM_EPOCHS = 'num_epochs'
LEARNING_RATE = 'learning_rate'
INPUT_DROPOUT = 'input_dropout'
OUTPUT_DROPOUT = 'output_dropout'
FEATURE_MAP_DROPOUT = 'feature_map_dropout'
#CNN related
NUM_IN_CHANNELS = 'num_input_channel'
NUM_OUT_CHANNELS = 'num_output_channels'
KERNEL_HEIGHT = 'kernel_height'
KERNEL_WIDTH = 'kernel_width'
IMAGE_HEIGHT = 'image_height'
IMAGE_WIDTH = 'image_width'

# Further Constants
SEED = 'seed'

