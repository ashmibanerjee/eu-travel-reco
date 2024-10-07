# eu-travel-reco


## Fine-Tuning

* Gemma-2b fine-tuned on 2 Nvidia A40 GPUs
* 10 epochs
* 1e-5 learning rate
* Model:
* Data:
  * Wikivoyage (English) data for 160 European cities.
  * Used Gemini 1.5 Pro and Flash to extract relevant questions from the data.


### Todo

- [ ] Evaluate data quality
- [ ] Evaluate model performance
  - [ ] Compare with baseline
- [ ] Build Demo