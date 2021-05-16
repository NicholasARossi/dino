
from video_generation import VideoGenerator





if __name__ == '__main__':
    class Arguments:
        input_path='ice2.mp4'
        video_only=False
        arch='deit_small'
        patch_size=8
        pretrained_weights='dino_deitsmall8_pretrain.pth'
        checkpoint_key="teacher"
        output_path='output'
        resize=None
        threshold=0.6


    vg=VideoGenerator(Arguments)
    vg.run()

