#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: chunk

short_description: List chunker

version_added: "X.X"

description:
    - "Allow you to chunk list in sub list of a given size."

options:
    src:
        description:
            - The list to be chunked
        required: true
        type: list
    size:
        description:
            - Define the chunk size
        required: true
        type: int

author:
    - Guillaume Marmorat (@marmorag)
'''

EXAMPLES = '''
# Encrypt data
- name: Chunk list
  chunk:
    src: [0,1,2,3,4]
    size: 2
  register: chunked
'''

RETURN = '''
chunks:
    description: List with sub list containing you items
    type: list
    returned: always
'''
from ansible.module_utils.basic import AnsibleModule

class Chunk:
    def __init__(self, module):
        self.module = module
        self.src = self.module.params['src']
        self.size = self.module.params['size']
        self.result = dict(
            changed=False,
            chunks=[]
        )

    def run(self):
        if self.module.check_mode:
            self.module.exit_json(**self.result)

        self.chunks()

        self.module.exit_json(**self.result)
    
    def chunks(self):
        self.result.chunks = [self.src[i:i + self.size] for i in range(0, len(self.src), self.size)]


def run_module():
    module_args = dict(
        src=dict(type='list', required=True),
        size=dict(type='int', required=True),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    Chunk(module).run()


def main():
    run_module()


if __name__ == '__main__':
    main()