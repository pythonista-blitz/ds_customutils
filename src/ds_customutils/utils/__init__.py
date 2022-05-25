import os
import random
from collections.abc import MutableMapping

import numpy as np
import requests
import torch


def flatten_dict(d: MutableMapping, parent_key: str = None, sep: str = ".") -> MutableMapping:
    """flatten multi-level dictionary

    Args:
        d (MutableMapping): multi-level dictionary
        parent_key (str, optional): prefix. Defaults to "".
        sep (str, optional): separator between parents-level and child. Defaults to ".".

    Returns:
        dict: flat dict
    """
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def set_seed(seed=42):
    """Sets the seed of the entire notebook so results are the same every time we run.
    This is for REPRODUCIBILITY."""
    np.random.seed(seed)
    random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    # When running on the CuDNN backend, two further options must be set
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    # Set a fixed value for the hash seed
    os.environ["PYTHONHASHSEED"] = str(seed)


def send_line_notify(notification_message: str, token: str) -> None:
    """LINE Notification function

    Args:
        notification_message (str): message content
        token (str): token for line notify
    """
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers=headers, data=data)
