from models import *

if __name__ == '__main__':
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    cfgpath = 'cfg/csdarknet53s-panet-spp.cfg'
    weights = 'weights/best8x-514.pt'
    target_weight = 'weights/yolobile.weights'
    model = Darknet(cfgpath)
    model.load_state_dict(torch.load(weights, map_location=device)['model'], strict=False)
    model.to(device)
    model.eval()

    save_weights(model, path=target_weight, cutoff=-1)