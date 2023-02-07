REGISTRY = {}

from .rnn_agent import RNNAgent
from .ff_agent import FFAgent
from .central_rnn_agent import CentralRNNAgent
from.central_ff_agent import CentralFFAgent

REGISTRY["rnn"] = RNNAgent
REGISTRY["ff"] = FFAgent

REGISTRY["central_rnn"] = CentralRNNAgent
REGISTRY["central_ff"] = CentralFFAgent