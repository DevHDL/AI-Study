## Abstract
<ins>시퀀스 변환 모델(sequence transduction models)</ins>은 <ins>인코더</ins>와 <ins>디코더</ins>를 포함하는 복잡한 반복 또는 CNN을 기반으로 한다.  
가장 성능이 좋은 모델도 <ins>주의 메커니즘(attention mechanism)</ins>을 통해 인코더와 디코더를 연결한다.  
본 논문에는 주의 메커니즘만을 기반으로 한 Transformer를 제안, recurrence와 convolution을 완전히 배제한다.  

두 가지 기계 번역 작업에 대한 실험에서 해당 모델은 우수한 성능과 병렬화가 가능하고 훈련에 훨씬 적은 시간이 소요된다.  
영어-독일어 번역 작업에서 기존 최고 결과보다 2BLEU 이상 개선되었다.  
영어-프랑스어 번역 작업에서 해당 모델은 8개의 GPU에서 3.5일간 훈련하여 41.8 BLEU 최고 점수를 획득했다.  
대규모 훈련 데이터와 제한된 훈련 데이터 모두에서 Transformer가 우수했고, 일반화 성능도 우수함을 보여준다.

### Keywords
- 시퀀스 변환 모델
- 인코더, 디코더
- 주의 메커니즘
- BLEU