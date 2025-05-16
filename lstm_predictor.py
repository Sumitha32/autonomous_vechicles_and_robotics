
import torch.nn as nn
import torch

class LSTMBehaviorPredictor(nn.Module):
    def __init__(self, input_size=4, hidden_size=128, output_size=1):
        super(LSTMBehaviorPredictor, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.linear = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        output = self.linear(lstm_out[:, -1, :])
        return output
