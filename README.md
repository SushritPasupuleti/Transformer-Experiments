# Transformer Experiments

Trying out a few transformer models

## Setup

Create venv:

```bash
python3 -m venv dev_venv
```

Source venv:

```bash
source dev_venv/bin/activate
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

Prepare/Update `requirements.txt`:

```bash
pip3 freeze > requirements.txt
```

### (Conditional) Rust Compiler Dependency

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Add the following to `PATH`:

```rc
$HOME/.cargo/bin
```

Check installation:

```bash
rustc --version
```

### (MacOS only)

```bash
pip3 install tensorflow-macos tensorflow-metal
```

