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
"""Describe maintenance policy command."""
from googlecloudsdk.api_lib.compute import base_classes
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.compute import flags as compute_flags
from googlecloudsdk.command_lib.compute.maintenance_policies import flags


class Describe(base.DescribeCommand):
  """Describes a Google Compute Engine maintenance policy."""

  @staticmethod
  def Args(parser):
    flags.MakeMaintenancePolicyArg().AddArgument(parser)

  def Run(self, args):
    holder = base_classes.ComputeApiHolder(self.ReleaseTrack())
    client = holder.client

    policy_ref = flags.MakeMaintenancePolicyArg().ResolveAsResource(
        args,
        holder.resources,
        scope_lister=compute_flags.GetDefaultScopeLister(holder.client))

    messages = holder.client.messages
    request = messages.ComputeMaintenancePoliciesGetRequest(
        maintenancePolicy=policy_ref.Name(),
        project=policy_ref.project,
        region=policy_ref.region)

    service = holder.client.apitools_client.maintenancePolicies
    return client.MakeRequests([(service, 'Get', request)])[0]
