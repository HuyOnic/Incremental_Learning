python main_rmm.py \
    -model rmm-foster \
    --dataset imagenet1000 \
    -ms 20000 \
    -init 500 \
    -incre 100 \
    -net cosine_resnet18 \
    -p benchmark \
    -d 3 \
    -c 0.0 0.0 0.1 0.1 0.1 0.0 \
    -m 0.3 0.3 0.3 0.4 0.4 0.4