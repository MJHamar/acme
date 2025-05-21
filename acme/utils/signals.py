# Copyright 2018 DeepMind Technologies Limited. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Helper methods for handling signals."""

import contextlib
import ctypes
import threading
from typing import Any, Callable, Optional

_Handler = Callable[[], Any]


@contextlib.contextmanager
def runtime_terminator(callback: Optional[_Handler] = None):
  # this is a noop. we don't need launchpad dependencies
  pass
