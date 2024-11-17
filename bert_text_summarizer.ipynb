{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "view-in-github"
   },
   "source": [
    "<a href=\"https://colab.research.google.com/github/patrick-nanys/text-summarization/blob/main/bert_text_summarizer.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "8CLvBco2J-xK"
   },
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "_UuFF0cEMktj",
    "outputId": "9c43bef6-1b7f-4108-d25c-159898829839"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mounted at /content/drive\n"
     ]
    }
   ],
   "source": [
    "from google.colab import drive\n",
    "drive.mount('/content/drive')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "7LBh9Octlhfs"
   },
   "outputs": [],
   "source": [
    "!cp drive/MyDrive/Colab\\ Notebooks/Deep\\ learning/reviews.xlsx reviews.xlsx"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "pGZDgfz_a6HG"
   },
   "source": [
    "###1. Data load from xlsx \n",
    "\n",
    "> Source: https://www.kaggle.com/shashichander009/inshorts-news-data\n",
    "> Source2.0: https://www.kaggle.com/snap/amazon-fine-food-reviews\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "FAEriAFohCba",
    "outputId": "5259c472-3843-4f92-c7d5-86fb52f21f9e"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    I have bought several of the Vitality canned d...\n",
      "1    Product arrived labeled as Jumbo Salted Peanut...\n",
      "2    This is a confection that has been around a fe...\n",
      "3    If you are looking for the secret ingredient i...\n",
      "4    Great taffy at a great price.  There was a wid...\n",
      "Name: Short, dtype: object 0    Good Quality Dog Food\n",
      "1        Not as Advertised\n",
      "2    \"Delight\" says it all\n",
      "3           Cough Medicine\n",
      "4              Great taffy\n",
      "Name: Headline, dtype: object\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "#xls = pd.read_excel(\"Inshorts Cleaned Data.xlsx\")\n",
    "xls = pd.read_excel(\"reviews.xlsx\")\n",
    "xls['headline_type'] = xls['Headline'].apply(type)\n",
    "xls.drop(xls[xls.headline_type != str].index, inplace=True)\n",
    "# Load articles, stories\n",
    "input_raw = xls['Short']\n",
    "# Load headlines for articles and stories\n",
    "output_raw = xls['Headline']\n",
    "\n",
    "# Show example\n",
    "print(input_raw.head(), output_raw.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 173
    },
    "id": "_WlCObs9bLdr",
    "outputId": "a36c545f-c8c7-44cb-8049-894d70801698"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Headline</th>\n",
       "      <th>Short</th>\n",
       "      <th>headline_type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>568427</td>\n",
       "      <td>568427</td>\n",
       "      <td>568427</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>295742</td>\n",
       "      <td>393576</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>Delicious!</td>\n",
       "      <td>This review will make me sound really stupid, ...</td>\n",
       "      <td>&lt;class 'str'&gt;</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>2462</td>\n",
       "      <td>199</td>\n",
       "      <td>568427</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Headline  ...  headline_type\n",
       "count       568427  ...         568427\n",
       "unique      295742  ...              1\n",
       "top     Delicious!  ...  <class 'str'>\n",
       "freq          2462  ...         568427\n",
       "\n",
       "[4 rows x 3 columns]"
      ]
     },
     "execution_count": 46,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "xls.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "yvwB6yxDOIB7"
   },
   "source": [
    "Obtaining length data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "ZVFDLC_pg0FQ",
    "outputId": "60047b32-9fee-4b27-b073-898cade41ed7"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Inputs:\n",
      " count    568427.000000\n",
      "mean        436.239369\n",
      "std         445.354882\n",
      "min          12.000000\n",
      "25%         179.000000\n",
      "50%         302.000000\n",
      "75%         527.000000\n",
      "max       21409.000000\n",
      "dtype: float64\n",
      "Outputs:\n",
      " count    568427.000000\n",
      "mean         23.446990\n",
      "std          14.028431\n",
      "min           1.000000\n",
      "25%          13.000000\n",
      "50%          20.000000\n",
      "75%          30.000000\n",
      "max         128.000000\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "input_lengths = pd.Series([len(x) for x in input_raw])\n",
    "output_lengths = pd.Series([len(str(x)) for x in output_raw])\n",
    "print('Inputs:\\n', input_lengths.describe())\n",
    "print('Outputs:\\n', output_lengths.describe())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "fvKS-MbphCPK"
   },
   "outputs": [],
   "source": [
    "# maxlen\n",
    "# taking values > and round figured to 75th percentile\n",
    "# at the same time not leaving high variance\n",
    "encoder_maxlen = 510 + 2\n",
    "decoder_maxlen = 30 + 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "xL15_ImQtNup"
   },
   "outputs": [],
   "source": [
    "def dataset_split(X, Y, valid_split, test_split):\n",
    "  v_start = int(len(X)*(1-valid_split-test_split))\n",
    "  t_start = int(len(X)*(1-test_split))\n",
    "  X_train, Y_train = X[:v_start], Y[:v_start]\n",
    "  X_valid, Y_valid = X[v_start:t_start], Y[v_start:t_start]\n",
    "  X_test , Y_test  = X[t_start:], Y[t_start:]\n",
    "  return X_train, Y_train, X_valid, Y_valid, X_test, Y_test"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "DYV8LFbQFct4"
   },
   "source": [
    "### Bert tokenization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "-gH7g-ICoD2N"
   },
   "outputs": [],
   "source": [
    "!rm -r uncased_L-12_H-768_A-12"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "0Yh2oOXOFg8f",
    "outputId": "8d93e691-be04-45f2-bd60-93c26a21ca72"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: bert-for-tf2 in /usr/local/lib/python3.6/dist-packages (0.14.7)\n",
      "Requirement already satisfied: params-flow>=0.8.0 in /usr/local/lib/python3.6/dist-packages (from bert-for-tf2) (0.8.2)\n",
      "Requirement already satisfied: py-params>=0.9.6 in /usr/local/lib/python3.6/dist-packages (from bert-for-tf2) (0.9.7)\n",
      "Requirement already satisfied: numpy in /usr/local/lib/python3.6/dist-packages (from params-flow>=0.8.0->bert-for-tf2) (1.18.5)\n",
      "Requirement already satisfied: tqdm in /usr/local/lib/python3.6/dist-packages (from params-flow>=0.8.0->bert-for-tf2) (4.41.1)\n",
      "--2020-11-26 12:32:09--  https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip\n",
      "Resolving storage.googleapis.com (storage.googleapis.com)... 74.125.20.128, 74.125.142.128, 74.125.195.128, ...\n",
      "Connecting to storage.googleapis.com (storage.googleapis.com)|74.125.20.128|:443... connected.\n",
      "HTTP request sent, awaiting response... 200 OK\n",
      "Length: 407727028 (389M) [application/zip]\n",
      "Saving to: ‘uncased_L-12_H-768_A-12.zip’\n",
      "\n",
      "uncased_L-12_H-768_ 100%[===================>] 388.84M   262MB/s    in 1.5s    \n",
      "\n",
      "2020-11-26 12:32:11 (262 MB/s) - ‘uncased_L-12_H-768_A-12.zip’ saved [407727028/407727028]\n",
      "\n",
      "Archive:  uncased_L-12_H-768_A-12.zip\n",
      "   creating: uncased_L-12_H-768_A-12/\n",
      "  inflating: uncased_L-12_H-768_A-12/bert_model.ckpt.meta  \n",
      "  inflating: uncased_L-12_H-768_A-12/bert_model.ckpt.data-00000-of-00001  \n",
      "  inflating: uncased_L-12_H-768_A-12/vocab.txt  \n",
      "  inflating: uncased_L-12_H-768_A-12/bert_model.ckpt.index  \n",
      "  inflating: uncased_L-12_H-768_A-12/bert_config.json  \n"
     ]
    }
   ],
   "source": [
    "# bert setup\n",
    "\n",
    "!pip install bert-for-tf2\n",
    "!wget https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip\n",
    "!unzip uncased_L-12_H-768_A-12.zip\n",
    "\n",
    "import os\n",
    "import bert\n",
    "import tensorflow as tf\n",
    "from bert import BertModelLayer\n",
    "from bert.loader import StockBertConfig, map_stock_config_to_params, load_stock_weights\n",
    "from bert.tokenization.bert_tokenization import FullTokenizer\n",
    "\n",
    "bert_model_name=\"uncased_L-12_H-768_A-12\"\n",
    "bert_ckpt_file = os.path.join(bert_model_name, \"bert_model.ckpt\")\n",
    "bert_config_file = os.path.join(bert_model_name, \"bert_config.json\")\n",
    "\n",
    "def create_bert_layer():\n",
    "  with tf.io.gfile.GFile(bert_config_file, \"r\") as reader:\n",
    "    bc = StockBertConfig.from_json_string(reader.read())\n",
    "    bert_params = map_stock_config_to_params(bc)\n",
    "    bert_params.adapter_size = None\n",
    "    bert = BertModelLayer.from_params(bert_params, name=\"bert\")\n",
    "  return bert\n",
    "\n",
    "# call this after build\n",
    "#load_stock_weights(bert, bert_ckpt_file)\n",
    "\n",
    "tokenizer = FullTokenizer(vocab_file=os.path.join(bert_model_name, \"vocab.txt\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "U_IQbjOeDbcz"
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from tqdm.notebook import tqdm\n",
    "\n",
    "def bert_tokenize(data):\n",
    "  tokenized_data = []\n",
    "  for text in tqdm(data):\n",
    "    tokens = tokenizer.tokenize(text)\n",
    "    tokens = [\"[CLS]\"] + tokens + [\"[SEP]\"]\n",
    "    token_ids = tokenizer.convert_tokens_to_ids(tokens)\n",
    "    tokenized_data.append(token_ids)\n",
    "  return tokenized_data\n",
    "\n",
    "def bert_pad(data, maxlen):\n",
    "  padded_data = []\n",
    "  for token_ids in tqdm(data):\n",
    "    token_ids = token_ids[:min(len(token_ids), maxlen - 2)]\n",
    "    token_ids = token_ids + [0] * (maxlen - len(token_ids))\n",
    "    padded_data.append(np.array(token_ids))\n",
    "  return np.array(padded_data)\n",
    "\n",
    "def bert_preprocess(data, maxlen):\n",
    "  print('tokenizing...')\n",
    "  x = bert_tokenize(data)\n",
    "  print('padding...')\n",
    "  x = bert_pad(x, maxlen)\n",
    "  return x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 315,
     "referenced_widgets": [
      "51c2bb2bb2364e5887094ebe6da2cadb",
      "718cbd32ab964b7280503b7a3f05b01e",
      "078a09e9c9a8495bbcd008c2c91cf33e",
      "c61ce0f5715542a68011c3b048f7fd93",
      "78b46ce5dac74bd8a91c99e200b853e7",
      "c3d3d8ef26eb436a88fb10b87fc8fd5c",
      "a27eda090306487b97ae51dc3157cddf",
      "f7eb589db4514c4e93e49ec174897619",
      "2b1ec8f77cd64989b4b009111ffa5554",
      "f6894cc94551463e969b9404f3c1c313",
      "464e34752e6048a0970081d687e49e96",
      "61a6791dd6ce4d26bf7d13e395d441da",
      "feb8dee5f5464068a8f5c8fe36879580",
      "6012e802455a48ecb79be562f215461a",
      "b8bb7cf43aeb4e7b9c85dbe3fc5ef157",
      "412a54aaae924565b9eac11d81ac1b89",
      "77d546d98b784fed9c73460fc9a01ea5",
      "13130b217e554cb587784d0a770dbcf1",
      "c1c90cee148c4165a278d8ae4afe4993",
      "f12ec219469d4e049ebc2b5a9fa66f2c",
      "52109b19d4584b10b245ae40991938cd",
      "c35f7d5d4c754470a712f4e882171b7b",
      "05b353224a8b4273a271000e465062c0",
      "436262dd36514b8a92dadcef46a5dcbe",
      "d71977aa37c945f9a7931cd7e3a69148",
      "a1af1fd33c574f29a1a53b77696cd224",
      "003a2a1aa3ad4ed8929b0640457dc63c",
      "6e45f8f122a14b3a8ce619307baa203c",
      "b90e5320ee69477bbcffd5ffdbaee4c6",
      "fab6a7f1616d4e3991a52ba7b6e5a578",
      "f62044dd6ca34f59960745f4b5e481a7",
      "59cf2e525161465fa493afe7a6f5b923"
     ]
    },
    "id": "yM-xrwkILuNl",
    "outputId": "220afb94-45d1-4da1-ecfc-0ff7f2162ca5"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Preprocessing input\n",
      "tokenizing...\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "51c2bb2bb2364e5887094ebe6da2cadb",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(FloatProgress(value=0.0, max=50000.0), HTML(value='')))"
      ]
     },
     "metadata": {
      "tags": []
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "padding...\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2b1ec8f77cd64989b4b009111ffa5554",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(FloatProgress(value=0.0, max=50000.0), HTML(value='')))"
      ]
     },
     "metadata": {
      "tags": []
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Preprocessing output\n",
      "tokenizing...\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "77d546d98b784fed9c73460fc9a01ea5",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(FloatProgress(value=0.0, max=50000.0), HTML(value='')))"
      ]
     },
     "metadata": {
      "tags": []
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "padding...\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d71977aa37c945f9a7931cd7e3a69148",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(FloatProgress(value=0.0, max=50000.0), HTML(value='')))"
      ]
     },
     "metadata": {
      "tags": []
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    }
   ],
   "source": [
    "print('Preprocessing input')\n",
    "X = bert_preprocess(input_raw[:50000], encoder_maxlen)\n",
    "print('Preprocessing output')\n",
    "Y = bert_preprocess(output_raw[:50000], decoder_maxlen)\n",
    "X_train, Y_train, X_valid, Y_valid, X_test, Y_test = dataset_split(X, Y, valid_split=0.2, test_split=0.1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "aK66hJ7wR_U6"
   },
   "outputs": [],
   "source": [
    "# save preprocessed reviews\n",
    "import pickle\n",
    "\n",
    "with open('preprocessed_reviews.pkl', 'wb') as file:\n",
    "  data = (X, Y)\n",
    "  pickle.dump(data, file)\n",
    "\n",
    "!cp preprocessed_reviews.pkl drive/MyDrive/Colab\\ Notebooks/Deep\\ learning/preprocessed_reviews.pkl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "pN8lCKGcStEN"
   },
   "outputs": [],
   "source": [
    "# load preprocessed reviews\n",
    "import pickle\n",
    "\n",
    "!cp drive/MyDrive/Colab\\ Notebooks/Deep\\ learning/preprocessed_reviews.pkl preprocessed_reviews.pkl\n",
    "\n",
    "with open('preprocessed_reviews.pkl', 'rb') as file:\n",
    "  data = pickle.load(file)\n",
    "\n",
    "nX, nY = data\n",
    "X_train, Y_train, X_valid, Y_valid, X_test, Y_test = dataset_split(nX, nY, valid_split=0.2, test_split=0.1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "9a7_42h4XafE",
    "outputId": "e4ae3f1f-6426-4926-c576-e709dc7701ef"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((35000, 512), (35000, 32), (10000, 512), (10000, 32), (5000, 512), (5000, 32))"
      ]
     },
     "execution_count": 57,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train.shape, Y_train.shape, X_valid.shape, Y_valid.shape, X_test.shape, Y_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "5AjkbDf1aHlB",
    "outputId": "a682f95e-031e-42fc-bb80-fd20211cf515"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50000"
      ]
     },
     "execution_count": 58,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train.shape[0] + X_valid.shape[0] + X_test.shape[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "eaBzIB3DwG2q",
    "outputId": "e25aa31b-d8e9-4977-ea19-ec452b8a5bab"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(30522, 30522)"
      ]
     },
     "execution_count": 59,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_vocab = len(tokenizer.vocab)\n",
    "y_vocab = len(tokenizer.vocab)\n",
    "x_vocab, y_vocab"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "m3CZDeQA1HQD",
    "outputId": "a1996f02-f91c-4c80-fa06-7a88d5f25df1"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((32, 512), (32, 32))"
      ]
     },
     "execution_count": 60,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X[:32].shape, Y[:32].shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "GspMEDS-qs57"
   },
   "source": [
    "# Training"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "iiNQeGg3tbVN"
   },
   "outputs": [],
   "source": [
    "from tensorflow.keras import Model\n",
    "from tensorflow.keras.layers import Input, LSTM, Embedding, Dense, Concatenate, Attention, Dropout, Conv1D, Flatten"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "1RiyLPpasNOZ"
   },
   "source": [
    "### Architecture"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "J5xxRw3crc-3"
   },
   "outputs": [],
   "source": [
    "embedding_dim = 250 #50\n",
    "hidden_dim = 250 #60\n",
    "\n",
    "ENC_LSTM_NUM = 3 #3\n",
    "ENC_LSTM_DROPOUT = 0.4 #0.4\n",
    "ENC_LSTM_RECURRENT_DROPOUT = 0.4 #0.4\n",
    "\n",
    "CONV_FILTERS = 32\n",
    "CONV_KERNEL_SIZE = 3\n",
    "\n",
    "# Architecture\n",
    "\n",
    "bert_layer = create_bert_layer()\n",
    "bert_layer.trainable = False\n",
    "\n",
    "# Encoder\n",
    "enc_emb = bert_layer\n",
    "#enc_emb = Embedding(x_vocab, embedding_dim)\n",
    "enc_lstms = []\n",
    "for i in range(ENC_LSTM_NUM):\n",
    "  enc_lstms.append(LSTM(hidden_dim, return_sequences=True, return_state=True))\n",
    "dropout = Dropout(ENC_LSTM_DROPOUT)\n",
    "\n",
    "# Decoder\n",
    "#dec_emb = bert_layer\n",
    "dec_emb = Embedding(y_vocab, embedding_dim)\n",
    "dec_lstm = LSTM(hidden_dim, return_sequences=True, return_state=True)\n",
    "attn = Attention()\n",
    "concat = Concatenate()\n",
    "conv1d = Conv1D(CONV_FILTERS, CONV_KERNEL_SIZE, activation='relu')\n",
    "dec_fc = Dense(y_vocab, activation='softmax')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "eCRT-PAHsShB"
   },
   "source": [
    "### Building the model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "5cbN9TsFtxin",
    "outputId": "407f38fb-316e-408d-b87c-0c4dfafe8b7c"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Done loading 196 BERT weights from: uncased_L-12_H-768_A-12/bert_model.ckpt into <bert.model.BertModelLayer object at 0x7fd6760b34e0> (prefix:bert). Count of weights not found in the checkpoint was: [0]. Count of weights with mismatched shape: [0]\n",
      "Unused weights from checkpoint: \n",
      "\tbert/embeddings/token_type_embeddings\n",
      "\tbert/pooler/dense/bias\n",
      "\tbert/pooler/dense/kernel\n",
      "\tcls/predictions/output_bias\n",
      "\tcls/predictions/transform/LayerNorm/beta\n",
      "\tcls/predictions/transform/LayerNorm/gamma\n",
      "\tcls/predictions/transform/dense/bias\n",
      "\tcls/predictions/transform/dense/kernel\n",
      "\tcls/seq_relationship/output_bias\n",
      "\tcls/seq_relationship/output_weights\n",
      "Model: \"functional_5\"\n",
      "__________________________________________________________________________________________________\n",
      "Layer (type)                    Output Shape         Param #     Connected to                     \n",
      "==================================================================================================\n",
      "input_5 (InputLayer)            [(None, 512)]        0                                            \n",
      "__________________________________________________________________________________________________\n",
      "bert (BertModelLayer)           (None, 512, 768)     108890112   input_5[0][0]                    \n",
      "__________________________________________________________________________________________________\n",
      "lstm_12 (LSTM)                  [(None, 512, 250), ( 1019000     bert[0][0]                       \n",
      "__________________________________________________________________________________________________\n",
      "dropout_3 (Dropout)             (None, 512, 250)     0           lstm_12[0][0]                    \n",
      "                                                                 lstm_13[0][0]                    \n",
      "                                                                 lstm_14[0][0]                    \n",
      "__________________________________________________________________________________________________\n",
      "lstm_13 (LSTM)                  [(None, 512, 250), ( 501000      dropout_3[0][0]                  \n",
      "__________________________________________________________________________________________________\n",
      "lstm_14 (LSTM)                  [(None, 512, 250), ( 501000      dropout_3[1][0]                  \n",
      "                                                                 dropout_3[2][0]                  \n",
      "__________________________________________________________________________________________________\n",
      "input_6 (InputLayer)            [(None, None)]       0                                            \n",
      "__________________________________________________________________________________________________\n",
      "embedding_3 (Embedding)         (None, None, 250)    7630500     input_6[0][0]                    \n",
      "__________________________________________________________________________________________________\n",
      "lstm_15 (LSTM)                  [(None, None, 250),  501000      embedding_3[0][0]                \n",
      "                                                                 lstm_14[1][1]                    \n",
      "                                                                 lstm_14[1][2]                    \n",
      "__________________________________________________________________________________________________\n",
      "attention_3 (Attention)         (None, None, 250)    0           lstm_15[0][0]                    \n",
      "                                                                 lstm_14[1][0]                    \n",
      "__________________________________________________________________________________________________\n",
      "concatenate_3 (Concatenate)     (None, None, 500)    0           lstm_15[0][0]                    \n",
      "                                                                 attention_3[0][0]                \n",
      "__________________________________________________________________________________________________\n",
      "dense_3 (Dense)                 (None, None, 30522)  15291522    concatenate_3[0][0]              \n",
      "==================================================================================================\n",
      "Total params: 134,334,134\n",
      "Trainable params: 25,444,022\n",
      "Non-trainable params: 108,890,112\n",
      "__________________________________________________________________________________________________\n"
     ]
    }
   ],
   "source": [
    "# Building the model\n",
    "\n",
    "# Encoder\n",
    "encoder_input = Input(shape=(encoder_maxlen,))\n",
    "enc_emb_out = enc_emb(encoder_input)\n",
    "lstm_in = enc_emb_out\n",
    "for i in range(ENC_LSTM_NUM):\n",
    "  lstm_out, h, c = enc_lstms[i](lstm_in)\n",
    "  lstm_out = dropout(lstm_out)\n",
    "  lstm_in = lstm_out\n",
    "enc_output, enc_state_h, enc_state_c = enc_lstms[-1](lstm_in)\n",
    " \n",
    "# Decoder\n",
    "decoder_input = Input(shape=(None,))\n",
    "dec_emb_out = dec_emb(decoder_input)\n",
    "dec_output, dec_state_h, dec_state_c = dec_lstm(dec_emb_out, initial_state=[enc_state_h, enc_state_c])\n",
    "\n",
    "attn_out = attn([dec_output, enc_output])\n",
    "conv_out = concat([dec_output, attn_out])\n",
    "output = dec_fc(conv_out)\n",
    "\n",
    "model = Model([encoder_input, decoder_input], output)\n",
    "\n",
    "load_stock_weights(bert_layer, bert_ckpt_file)\n",
    "\n",
    "model.summary()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "JJVp_drem0hD"
   },
   "source": [
    "### Rouge loss function\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "02i_9RJbm5Lk"
   },
   "outputs": [],
   "source": [
    "import keras.backend as K\n",
    "\n",
    "def n_grams(n, text):\n",
    "  return [tuple(text[i:i+n]) for i in range(len(text)-n+1)]\n",
    "\n",
    "def rouge(y, y_pred):\n",
    "  total_words_in_reference = len(y)\n",
    "  recalls = []\n",
    "  for i in range(1, 4):\n",
    "    target_n_grams = set(np.vectorize(n_grams(i, y)))\n",
    "    pred_n_grams = set(np.vectorize(n_grams(i, y_pred)))\n",
    "    number_of_overlapping = target_n_grams.intersection(pred_n_grams)\n",
    "    recalls.append(number_of_overlapping / total_words_in_reference)\n",
    "  return K.mean(recalls)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "VhAQD6ctsE_C"
   },
   "outputs": [],
   "source": [
    "model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "QMMLl1zvRL_l"
   },
   "outputs": [],
   "source": [
    "!cp drive/MyDrive/Colab\\ Notebooks/Deep\\ learning/bert_model.hdf5 bert_model.hdf5\n",
    "model.load_weights('bert_model.hdf5')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "a44gkWMnsXlA"
   },
   "source": [
    "### Training"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "7GdBagPjoCA6"
   },
   "outputs": [],
   "source": [
    "def get_model_input(X, Y):\n",
    "  \"\"\"\n",
    "    List of X and Y where Ys last word is excluded\n",
    "  \"\"\"\n",
    "  return [X, Y[:,:-1]]\n",
    "\n",
    "def get_model_output(Y):\n",
    "  \"\"\"\n",
    "    Y input shifted right (first word excluded) and made it third dimensional\n",
    "  \"\"\"\n",
    "  return Y.reshape(Y.shape[0],Y.shape[1], 1)[:,1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "nlxBwsdmw4CT"
   },
   "outputs": [],
   "source": [
    "from tensorflow.keras.callbacks import EarlyStopping\n",
    "from tensorflow.keras.callbacks import ModelCheckpoint\n",
    "\n",
    "PATIENCE = 3\n",
    "SAVED_MODEL_PATH = 'bert_model.hdf5'\n",
    "\n",
    "earlystopping = EarlyStopping(patience=PATIENCE, monitor='val_loss', mode='min', verbose=1)\n",
    "checkpointer = ModelCheckpoint(filepath=SAVED_MODEL_PATH, save_best_only=True, verbose=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "VBjqAZ8Ik0o2",
    "outputId": "23ad1bcf-2067-4284-e582-e3d2483adac2"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/3\n",
      "1094/1094 [==============================] - 2465s 2s/step - loss: 0.8159 - val_loss: 0.9827\n",
      "Epoch 2/3\n",
      "1094/1094 [==============================] - 2460s 2s/step - loss: 0.8019 - val_loss: 0.9862\n",
      "Epoch 3/3\n",
      "1094/1094 [==============================] - 2460s 2s/step - loss: 0.7928 - val_loss: 0.9909\n"
     ]
    }
   ],
   "source": [
    "history = model.fit(\n",
    "    get_model_input(X_train, Y_train),\n",
    "    get_model_output(Y_train),\n",
    "    epochs=3, #20\n",
    "    batch_size=32, #32,\n",
    "    validation_data=(\n",
    "        get_model_input(X_valid, Y_valid),\n",
    "        get_model_output(Y_valid)\n",
    "        ),\n",
    "    callbacks=[checkpointer, earlystopping]\n",
    "    )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "4DCvmN94Wgey"
   },
   "source": [
    "loss: 1.2703 - val_loss: 1.1933\n",
    "\n",
    "loss: 1.0352 - val_loss: 1.0634\n",
    "\n",
    "loss: 0.9740 - val_loss: 1.0341\n",
    "\n",
    "loss: 0.9354 - val_loss: 1.0127\n",
    "\n",
    "loss: 0.9093 - val_loss: 1.0061\n",
    "\n",
    "loss: 0.8868 - val_loss: 0.9943\n",
    "\n",
    "loss: 0.8670 - val_loss: 0.9894\n",
    "\n",
    "loss: 0.8480 - val_loss: 0.9853\n",
    "\n",
    "loss: 0.8321 - val_loss: 0.9849\n",
    "\n",
    "loss: 0.8159 - val_loss: 0.9827\n",
    "\n",
    "loss: 0.8019 - val_loss: 0.9862\n",
    "\n",
    "loss: 0.7928 - val_loss: 0.9909"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "bGiH7V8kTVFv"
   },
   "outputs": [],
   "source": [
    "model.load_weights(SAVED_MODEL_PATH)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "8VBvDqMglOSo"
   },
   "outputs": [],
   "source": [
    "# save model\n",
    "!\\cp bert_model.hdf5 drive/MyDrive/Colab\\ Notebooks/Deep\\ learning/bert_model.hdf5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 282
    },
    "id": "R0iuV1w3jHy5",
    "outputId": "3bcba4c3-9958-44c6-f4af-fd44c562b951"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x7fd66f080be0>"
      ]
     },
     "execution_count": 72,
     "metadata": {
      "tags": []
     },
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light",
      "tags": []
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "\n",
    "sns.lineplot(data=history.history['loss'], label='train loss')\n",
    "sns.lineplot(data=history.history['val_loss'], label='val loss')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "h9jg-sYVqoS3"
   },
   "source": [
    "# Inference"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "iRtsDYqIyH3Z"
   },
   "outputs": [],
   "source": [
    "# Encode\n",
    "encoder_model = Model(encoder_input, [enc_output, enc_state_h, enc_state_c])\n",
    "\n",
    "# Inputs for decode\n",
    "dec_state_input_h = Input(shape=(hidden_dim,))\n",
    "dec_state_input_c = Input(shape=(hidden_dim,))\n",
    "dec_hidden_state_input = Input(shape=(encoder_maxlen, hidden_dim))\n",
    "\n",
    "# Decode\n",
    "dec_emb_out2 = dec_emb(decoder_input)\n",
    "dec_output2, dec_state_h2, dec_state_c2 = dec_lstm(dec_emb_out2, initial_state=[dec_state_input_h, dec_state_input_c])\n",
    "attn_out2 = attn([dec_output2, dec_hidden_state_input])\n",
    "concat_out2 = concat([dec_output2, attn_out2])\n",
    "output = dec_fc(concat_out2)\n",
    "\n",
    "decoder_model = Model([decoder_input] + [dec_hidden_state_input, dec_state_input_h, dec_state_input_c], [output] + [dec_state_h2, dec_state_c2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "WcjYXDL75LvC"
   },
   "outputs": [],
   "source": [
    "reverse_target_word_index=tokenizers[1].index_word\n",
    "reverse_source_word_index=tokenizers[0].index_word\n",
    "target_word_index=tokenizers[1].word_index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "LgtYRsN9T4rz"
   },
   "outputs": [],
   "source": [
    "reverse_target_word_index=lambda x: tokenizer.convert_ids_to_tokens([x])[0]\n",
    "reverse_source_word_index=lambda x: tokenizer.convert_ids_to_tokens([x])[0]\n",
    "target_word_index=lambda x: tokenizer.convert_tokens_to_ids([x])[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "7CqtUoHy32RK"
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "def decode_sequence(input_seq):\n",
    "  e_out, e_h, e_c = encoder_model.predict(input_seq)\n",
    "\n",
    "  target_seq = np.zeros((1, 1))\n",
    "  target_seq[0, 0] = target_word_index('[CLS]')\n",
    "\n",
    "  stop_condition = False\n",
    "  decoded_sentence = ''\n",
    "  while not stop_condition:\n",
    "\n",
    "    output_tokens, h, c = decoder_model.predict([target_seq] + [e_out, e_h, e_c])\n",
    "\n",
    "    # sample a token\n",
    "    sampled_token_index = np.argmax(output_tokens[0, -1, :])\n",
    "    try:\n",
    "      sampled_token = reverse_target_word_index(sampled_token_index)\n",
    "    except:\n",
    "      sampled_token = '[UNK]'\n",
    "\n",
    "    if(sampled_token!='[SEP]'):\n",
    "      decoded_sentence += ' '+sampled_token\n",
    "\n",
    "    # Exit condition: either hit max length or find stop word.\n",
    "    if (sampled_token == '[SEP]'  or len(decoded_sentence.split()) >= (decoder_maxlen - 1)):\n",
    "      stop_condition = True\n",
    "\n",
    "    # Update the target sequence (of length 1).\n",
    "    target_seq = np.zeros((1,1))\n",
    "    target_seq[0, 0] = sampled_token_index\n",
    "\n",
    "    # Update internal states\n",
    "    e_h, e_c = h, c\n",
    "\n",
    "  return decoded_sentence"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "1WXzdaDm9R1R"
   },
   "outputs": [],
   "source": [
    "def seq2summary(input_seq):\n",
    "    newString=''\n",
    "    for item in input_seq:\n",
    "        if(item != 0 and item != target_word_index('[CLS]') and item != target_word_index('[SEP]')):\n",
    "          try:\n",
    "            new_str = reverse_target_word_index(item)\n",
    "          except:\n",
    "            new_str = '[UNK]'\n",
    "          newString = newString + new_str + ' '\n",
    "    return newString\n",
    "\n",
    "def seq2text(input_seq):\n",
    "    newString=''\n",
    "    for item in input_seq:\n",
    "      if(item != 0):\n",
    "        try:\n",
    "          new_str = reverse_source_word_index(item)\n",
    "        except:\n",
    "          new_str = '[UNK]'\n",
    "        newString = newString + new_str + ' '\n",
    "    return newString"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "gks2rIBct9Qj",
    "outputId": "253800e9-0912-41c3-8217-ca75acf16102"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text: [CLS] i have bought several of the vital ##ity canned dog food products and have found them all to be of good quality . the product looks more like a stew than a processed meat and it smells better . my labrador is fin ##ick ##y and she appreciate ##s this product better than most . [SEP] \n",
      "Original title: good quality dog food \n",
      "Predicted title:  great dog food\n",
      "\n",
      "\n",
      "Text: [CLS] product arrived labeled as ju ##mbo salt ##ed peanuts . . . the peanuts were actually small sized un ##sal ##ted . not sure if this was an error or if the vendor intended to represent the product as \" ju ##mbo \" . [SEP] \n",
      "Original title: not as advertised \n",
      "Predicted title:  not as good as the money\n",
      "\n",
      "\n",
      "Text: [CLS] this is a con ##fect ##ion that has been around a few centuries . it is a light , pillow ##y citrus gel ##atin with nuts - in this case fi ##lbert ##s . and it is cut into tiny squares and then liberal ##ly coated with powder ##ed sugar . and it is a tiny mouthful of heaven . not too chew ##y , and very flavor ##ful . i highly recommend this yu ##mmy treat . if you are familiar with the story of c . s . lewis ' \" the lion , the witch , and the wardrobe \" - this is the treat that seduce ##s edmund into selling out his brother and sisters to the witch . [SEP] \n",
      "Original title: \" delight \" says it all \n",
      "Predicted title:  great for a snack\n",
      "\n",
      "\n",
      "Text: [CLS] if you are looking for the secret ingredient in rob ##it ##uss ##in i believe i have found it . i got this in addition to the root beer extract i ordered ( which was good ) and made some cherry soda . the flavor is very medicinal . [SEP] \n",
      "Original title: cough medicine \n",
      "Predicted title:  great product\n",
      "\n",
      "\n",
      "Text: [CLS] great ta ##ffy at a great price . there was a wide assortment of yu ##mmy ta ##ffy . delivery was very quick . if your a ta ##ffy lover , this is a deal . [SEP] \n",
      "Original title: great ta ##ffy \n",
      "Predicted title:  great snack\n",
      "\n",
      "\n",
      "Text: [CLS] i got a wild hair for ta ##ffy and ordered this five pound bag . the ta ##ffy was all very enjoyable with many flavors : water ##mel ##on , root beer , mel ##on , pepper ##min ##t , grape , etc . my only complaint is there was a bit too much red / black li ##cor ##ice - flavor ##ed pieces ( just not my particular favorites ) . between me , my kids , and my husband , this lasted only two weeks ! i would recommend this brand of ta ##ffy - - it was a delightful treat . [SEP] \n",
      "Original title: nice ta ##ffy \n",
      "Predicted title:  great snack\n",
      "\n",
      "\n",
      "Text: [CLS] this salt ##water ta ##ffy had great flavors and was very soft and chew ##y . each candy was individually wrapped well . none of the candi ##es were stuck together , which did happen in the expensive version , fra ##linger ' s . would highly recommend this candy ! i served it at a beach - themed party and everyone loved it ! [SEP] \n",
      "Original title: great ! just as good as the expensive brands ! \n",
      "Predicted title:  delicious !\n",
      "\n",
      "\n",
      "Text: [CLS] this ta ##ffy is so good . it is very soft and chew ##y . the flavors are amazing . i would definitely recommend you buying it . very satisfying ! ! [SEP] \n",
      "Original title: wonderful , ta ##sty ta ##ffy \n",
      "Predicted title:  yu ##mmy !\n",
      "\n",
      "\n",
      "Text: [CLS] right now i ' m mostly just sp ##rou ##ting this so my cats can eat the grass . they love it . i rotate it around with wheat ##grass and rye too [SEP] \n",
      "Original title: ya ##y barley \n",
      "Predicted title:  great food\n",
      "\n",
      "\n",
      "Text: [CLS] this is a very healthy dog food . good for their digest ##ion . also good for small pup ##pies . my dog eats her required amount at every feeding . [SEP] \n",
      "Original title: healthy dog food \n",
      "Predicted title:  great dog food\n",
      "\n",
      "\n",
      "Text: [CLS] i don ' t know if it ' s the cactus or the tequila or just the unique combination of ingredients , but the flavour of this hot sauce makes it one of a kind ! we picked up a bottle once on a trip we were on and brought it back home with us and were totally blown away ! when we realized that we simply couldn ' t find it anywhere in our city we were bum ##med . < br / > < br / > now , because of the magic of the internet , we have a case of the sauce and are ec ##static because of it . < br / > < br / > if you love hot sauce . . i mean really love hot sauce , but don ' t want a sauce that taste ##lessly burns your throat , grab a bottle of tequila pic ##ante go ##ur ##met de inc ##lan . just realize that once you taste it , you will never want to use any other sauce . < br / > < br / > thank you for the personal , incredible service ! [SEP] \n",
      "Original title: the best hot sauce in the world \n",
      "Predicted title:  great product , great price !\n",
      "\n",
      "\n",
      "Text: [CLS] one of my boys needed to lose some weight and the other didn ' t . i put this food on the floor for the chu ##bby guy , and the protein - rich , no by - product food up higher where only my skinny boy can jump . the higher food sits going stale . they both really go for this food . and my chu ##bby boy has been losing about an ounce a week . [SEP] \n",
      "Original title: my cats love this \" diet \" food better than their regular food \n",
      "Predicted title:  great food , but not as good as the cats\n",
      "\n",
      "\n",
      "Text: [CLS] my cats have been happily eating fe ##lidae platinum for more than two years . i just got a new bag and the shape of the food is different . they tried the new food when i first put it in their bowls and now the bowls sit full and the kit ##ties will not touch the food . i ' ve noticed similar reviews related to formula changes in the past . unfortunately , i now need to find a new food that my cats will eat . [SEP] \n",
      "Original title: my cats are not fans of the new food \n",
      "Predicted title:  great food , but not as good as the cats\n",
      "\n",
      "\n",
      "Text: [CLS] good flavor ! these came securely packed . . . they were fresh and delicious ! i love these t ##wi ##zzle ##rs ! [SEP] \n",
      "Original title: fresh and greasy ! \n",
      "Predicted title:  yu ##mmy !\n",
      "\n",
      "\n",
      "Text: [CLS] the strawberry t ##wi ##zzle ##rs are my guilty pleasure - yu ##mmy . six pounds will be around for a while with my son and i . [SEP] \n",
      "Original title: strawberry t ##wi ##zzle ##rs - yu ##mmy \n",
      "Predicted title:  great product\n",
      "\n",
      "\n",
      "Text: [CLS] my daughter loves t ##wi ##zzle ##rs and this shipment of six pounds really hit the spot . it ' s exactly what you would expect . . . six packages of strawberry t ##wi ##zzle ##rs . [SEP] \n",
      "Original title: lots of t ##wi ##zzle ##rs , just what you expect . \n",
      "Predicted title:  great product\n",
      "\n",
      "\n",
      "Text: [CLS] i love eating them and they are good for watching tv and looking at movies ! it is not too sweet . i like to transfer them to a zip lock bag ##gie so they stay fresh so i can take my time eating them . [SEP] \n",
      "Original title: poor taste \n",
      "Predicted title:  great snack\n",
      "\n",
      "\n",
      "Text: [CLS] i am very satisfied with my t ##wi ##zzle ##r purchase . i shared these with others and we have all enjoyed them . i will definitely be ordering more . [SEP] \n",
      "Original title: love it ! \n",
      "Predicted title:  great product\n",
      "\n",
      "\n",
      "Text: [CLS] t ##wi ##zzle ##rs , strawberry my childhood favorite candy , made in lancaster pennsylvania by y & s candi ##es , inc . one of the oldest con ##fect ##ion ##ery firms in the united states , now a subsidiary of the hers ##hey company , the company was established in 1845 as young and sm ##yl ##ie , they also make apple li ##cor ##ice twists , green color and blue ras ##p ##berry li ##cor ##ice twists , i like them all < br / > < br / > i keep it in a dry cool place because is not recommended it to put it in the fridge . according to the guinness book of records , the longest li ##cor ##ice twist ever made measured 1 . 200 feet ( 370 m ) and weighted 100 pounds ( 45 kg ) and was made by y & s candi ##es , inc . this record - breaking twist became a guinness world record on july 19 , 1998 . this product is ko ##sher ! thank you [SEP] \n",
      "Original title: great sweet candy ! \n",
      "Predicted title:  delicious !\n",
      "\n",
      "\n",
      "Text: [CLS] candy was delivered very fast and was purchased at a reasonable price . i was home bound and unable to get to a store so this was perfect for me . [SEP] \n",
      "Original title: home delivered t ##wi ##zle ##rs \n",
      "Predicted title:  great product\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "for i in range(20):\n",
    "    print(\"Text:\",seq2text(X_train[i]))\n",
    "    print(\"Original title:\",seq2summary(Y_train[i]))\n",
    "    print(\"Predicted title:\",decode_sequence(X_train[i].reshape(1, -1)))\n",
    "    print(\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "-eIj3AXi46sE"
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "accelerator": "GPU",
  "colab": {
   "collapsed_sections": [
    "h0CyGJ3cgoT0",
    "eF4knn3xhpj8",
    "yJiyIJYciIgT",
    "QqLinn2u88J6",
    "papK44dU9hRk"
   ],
   "include_colab_link": true,
   "name": "bert_text_summarizer.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "name": "python3"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "003a2a1aa3ad4ed8929b0640457dc63c": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "FloatProgressModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "FloatProgressModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "ProgressView",
      "bar_style": "success",
      "description": "100%",
      "description_tooltip": null,
      "layout": "IPY_MODEL_fab6a7f1616d4e3991a52ba7b6e5a578",
      "max": 50000,
      "min": 0,
      "orientation": "horizontal",
      "style": "IPY_MODEL_b90e5320ee69477bbcffd5ffdbaee4c6",
      "value": 50000
     }
    },
    "05b353224a8b4273a271000e465062c0": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "DescriptionStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "DescriptionStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "description_width": ""
     }
    },
    "078a09e9c9a8495bbcd008c2c91cf33e": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "FloatProgressModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "FloatProgressModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "ProgressView",
      "bar_style": "success",
      "description": "100%",
      "description_tooltip": null,
      "layout": "IPY_MODEL_c3d3d8ef26eb436a88fb10b87fc8fd5c",
      "max": 50000,
      "min": 0,
      "orientation": "horizontal",
      "style": "IPY_MODEL_78b46ce5dac74bd8a91c99e200b853e7",
      "value": 50000
     }
    },
    "13130b217e554cb587784d0a770dbcf1": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "2b1ec8f77cd64989b4b009111ffa5554": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HBoxModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HBoxModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HBoxView",
      "box_style": "",
      "children": [
       "IPY_MODEL_464e34752e6048a0970081d687e49e96",
       "IPY_MODEL_61a6791dd6ce4d26bf7d13e395d441da"
      ],
      "layout": "IPY_MODEL_f6894cc94551463e969b9404f3c1c313"
     }
    },
    "412a54aaae924565b9eac11d81ac1b89": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "436262dd36514b8a92dadcef46a5dcbe": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "464e34752e6048a0970081d687e49e96": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "FloatProgressModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "FloatProgressModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "ProgressView",
      "bar_style": "success",
      "description": "100%",
      "description_tooltip": null,
      "layout": "IPY_MODEL_6012e802455a48ecb79be562f215461a",
      "max": 50000,
      "min": 0,
      "orientation": "horizontal",
      "style": "IPY_MODEL_feb8dee5f5464068a8f5c8fe36879580",
      "value": 50000
     }
    },
    "51c2bb2bb2364e5887094ebe6da2cadb": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HBoxModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HBoxModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HBoxView",
      "box_style": "",
      "children": [
       "IPY_MODEL_078a09e9c9a8495bbcd008c2c91cf33e",
       "IPY_MODEL_c61ce0f5715542a68011c3b048f7fd93"
      ],
      "layout": "IPY_MODEL_718cbd32ab964b7280503b7a3f05b01e"
     }
    },
    "52109b19d4584b10b245ae40991938cd": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "ProgressStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "ProgressStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "bar_color": null,
      "description_width": "initial"
     }
    },
    "59cf2e525161465fa493afe7a6f5b923": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "6012e802455a48ecb79be562f215461a": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "61a6791dd6ce4d26bf7d13e395d441da": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HTMLModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HTMLModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HTMLView",
      "description": "",
      "description_tooltip": null,
      "layout": "IPY_MODEL_412a54aaae924565b9eac11d81ac1b89",
      "placeholder": "​",
      "style": "IPY_MODEL_b8bb7cf43aeb4e7b9c85dbe3fc5ef157",
      "value": " 50000/50000 [00:02&lt;00:00, 18825.03it/s]"
     }
    },
    "6e45f8f122a14b3a8ce619307baa203c": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HTMLModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HTMLModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HTMLView",
      "description": "",
      "description_tooltip": null,
      "layout": "IPY_MODEL_59cf2e525161465fa493afe7a6f5b923",
      "placeholder": "​",
      "style": "IPY_MODEL_f62044dd6ca34f59960745f4b5e481a7",
      "value": " 50000/50000 [00:01&lt;00:00, 38629.56it/s]"
     }
    },
    "718cbd32ab964b7280503b7a3f05b01e": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "77d546d98b784fed9c73460fc9a01ea5": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HBoxModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HBoxModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HBoxView",
      "box_style": "",
      "children": [
       "IPY_MODEL_c1c90cee148c4165a278d8ae4afe4993",
       "IPY_MODEL_f12ec219469d4e049ebc2b5a9fa66f2c"
      ],
      "layout": "IPY_MODEL_13130b217e554cb587784d0a770dbcf1"
     }
    },
    "78b46ce5dac74bd8a91c99e200b853e7": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "ProgressStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "ProgressStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "bar_color": null,
      "description_width": "initial"
     }
    },
    "a1af1fd33c574f29a1a53b77696cd224": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "a27eda090306487b97ae51dc3157cddf": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "DescriptionStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "DescriptionStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "description_width": ""
     }
    },
    "b8bb7cf43aeb4e7b9c85dbe3fc5ef157": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "DescriptionStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "DescriptionStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "description_width": ""
     }
    },
    "b90e5320ee69477bbcffd5ffdbaee4c6": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "ProgressStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "ProgressStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "bar_color": null,
      "description_width": "initial"
     }
    },
    "c1c90cee148c4165a278d8ae4afe4993": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "FloatProgressModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "FloatProgressModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "ProgressView",
      "bar_style": "success",
      "description": "100%",
      "description_tooltip": null,
      "layout": "IPY_MODEL_c35f7d5d4c754470a712f4e882171b7b",
      "max": 50000,
      "min": 0,
      "orientation": "horizontal",
      "style": "IPY_MODEL_52109b19d4584b10b245ae40991938cd",
      "value": 50000
     }
    },
    "c35f7d5d4c754470a712f4e882171b7b": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "c3d3d8ef26eb436a88fb10b87fc8fd5c": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "c61ce0f5715542a68011c3b048f7fd93": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HTMLModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HTMLModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HTMLView",
      "description": "",
      "description_tooltip": null,
      "layout": "IPY_MODEL_f7eb589db4514c4e93e49ec174897619",
      "placeholder": "​",
      "style": "IPY_MODEL_a27eda090306487b97ae51dc3157cddf",
      "value": " 50000/50000 [01:34&lt;00:00, 530.51it/s]"
     }
    },
    "d71977aa37c945f9a7931cd7e3a69148": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HBoxModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HBoxModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HBoxView",
      "box_style": "",
      "children": [
       "IPY_MODEL_003a2a1aa3ad4ed8929b0640457dc63c",
       "IPY_MODEL_6e45f8f122a14b3a8ce619307baa203c"
      ],
      "layout": "IPY_MODEL_a1af1fd33c574f29a1a53b77696cd224"
     }
    },
    "f12ec219469d4e049ebc2b5a9fa66f2c": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "HTMLModel",
     "state": {
      "_dom_classes": [],
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "HTMLModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/controls",
      "_view_module_version": "1.5.0",
      "_view_name": "HTMLView",
      "description": "",
      "description_tooltip": null,
      "layout": "IPY_MODEL_436262dd36514b8a92dadcef46a5dcbe",
      "placeholder": "​",
      "style": "IPY_MODEL_05b353224a8b4273a271000e465062c0",
      "value": " 50000/50000 [00:31&lt;00:00, 1608.89it/s]"
     }
    },
    "f62044dd6ca34f59960745f4b5e481a7": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "DescriptionStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "DescriptionStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "description_width": ""
     }
    },
    "f6894cc94551463e969b9404f3c1c313": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "f7eb589db4514c4e93e49ec174897619": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "fab6a7f1616d4e3991a52ba7b6e5a578": {
     "model_module": "@jupyter-widgets/base",
     "model_name": "LayoutModel",
     "state": {
      "_model_module": "@jupyter-widgets/base",
      "_model_module_version": "1.2.0",
      "_model_name": "LayoutModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "LayoutView",
      "align_content": null,
      "align_items": null,
      "align_self": null,
      "border": null,
      "bottom": null,
      "display": null,
      "flex": null,
      "flex_flow": null,
      "grid_area": null,
      "grid_auto_columns": null,
      "grid_auto_flow": null,
      "grid_auto_rows": null,
      "grid_column": null,
      "grid_gap": null,
      "grid_row": null,
      "grid_template_areas": null,
      "grid_template_columns": null,
      "grid_template_rows": null,
      "height": null,
      "justify_content": null,
      "justify_items": null,
      "left": null,
      "margin": null,
      "max_height": null,
      "max_width": null,
      "min_height": null,
      "min_width": null,
      "object_fit": null,
      "object_position": null,
      "order": null,
      "overflow": null,
      "overflow_x": null,
      "overflow_y": null,
      "padding": null,
      "right": null,
      "top": null,
      "visibility": null,
      "width": null
     }
    },
    "feb8dee5f5464068a8f5c8fe36879580": {
     "model_module": "@jupyter-widgets/controls",
     "model_name": "ProgressStyleModel",
     "state": {
      "_model_module": "@jupyter-widgets/controls",
      "_model_module_version": "1.5.0",
      "_model_name": "ProgressStyleModel",
      "_view_count": null,
      "_view_module": "@jupyter-widgets/base",
      "_view_module_version": "1.2.0",
      "_view_name": "StyleView",
      "bar_color": null,
      "description_width": "initial"
     }
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
