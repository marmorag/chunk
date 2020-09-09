## chunk
[Ansible Galaxy collection](https://galaxy.ansible.com/marmorag/chunk) repository.\
Easily chunk your array to the size you want.

### My use case
While trying to remove objects from a S3 bucket, DeleteObjects directive limit to 1000 objects per call. Since the ListObjectsV2 return the whole list of objects,
I needed to chunk my objects list in smaller (in that case 5*1000 objects).

### Install

---

Install it via ansible-galaxy (recommended):

```bash
ansible-galaxy collection install marmorag.chunk
```

### Usage

---

```yamlex
- name: your list
  set_fact:
    your_list: [0,1,2,3,4]

- name: chunk list
  ansodium:
    src: "{{ your_list  }}"
    size: 2
```

Output format : 
```json
{
    "chunks": [[0,1], [2,3], [4]],
    "changed": true,
    "failed": false
}
```
