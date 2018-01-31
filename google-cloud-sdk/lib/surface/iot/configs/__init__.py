# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The configs command group for the Cloud IoT CLI."""
from googlecloudsdk.calliope import base


# TODO(b/64597141): Remove this command group when usage is low.
@base.Deprecate(
    is_removed=False,
    warning=('This command group is deprecated. Use \'gcloud iot devices '
             'configs\' instead.'))
@base.Hidden
class Configs(base.Group):
  """Manage configurations for Cloud IoT devices.

  Commands for managing configurations for Google Cloud IoT devices.
  """
