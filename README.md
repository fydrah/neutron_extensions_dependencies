# Neutron extension requirements

Simple python script to generate a extension dependencies graph.

## Usage

```
export OS_VERSION=rocky # stein, train,...
git checkout stable/$OS_VERSION

virtualenv venv
source venv/bin/activate

pip install -r requirements.txt
./graph.py [FILENAME]
```

Thanks @lukapeschke ;)
