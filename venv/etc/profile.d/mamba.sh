export MAMBA_ROOT_PREFIX="/workspaces/image-classifier/venv"
__mamba_setup="$("/workspaces/image-classifier/venv/bin/mamba" shell hook --shell posix 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__mamba_setup"
else
    alias mamba="/workspaces/image-classifier/venv/bin/mamba"  # Fallback on help from mamba activate
fi
unset __mamba_setup
