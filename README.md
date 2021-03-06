# Project_2
중고차_시세_분석_및_예측

![mini_project_2_image](https://user-images.githubusercontent.com/97490673/168200563-adf427b9-f82c-407b-9404-800ef71b04a3.jpg)

### 0. 개요
- 국토교통부의 통계에 따르면 중고차 거래건 수가 2019년 대비 7.2% 증가하였습니다. 
- 중고차 시장이 성장할 수 있던 배경에는 자동차의 품질과 내구성 향상이 큰 영역을 차지할 것으로 보입니다. 
- 중소벤처기업부는 생계형 적합업종 심의위원회를 열고 중고차 판매업을 생계형 적합업종으로 지정하지 않기로 결정하였습니다.
  - 현대자동차, 기아, 한국GM, 쌍용자동차, 르노코리아자동차 등 국내 완성차 업체의 중고차 진출이 가능해졌습니다. 
- kaggle data : https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes

### 1. for문_파일병합

### 2. 다중선형회귀분석

### 3. 릿지_라쏘_회귀모현

### 3.5. 주요 파라미터
- n_estimators	- 결정트리의 갯수를 지정
  - Default = 10
  - 무작정 트리 갯수를 늘리면 성능 좋아지는 것 대비 시간이 걸릴 수 있음
- min_samples_split	- 노드를 분할하기 위한 최소한의 샘플 데이터수 → 과적합을 제어하는데 사용
  - Default = 2 → 작게 설정할 수록 분할 노드가 많아져 과적합 가능성 증가

- min_samples_leaf	- 리프노드가 되기 위해 필요한 최소한의 샘플 데이터수
  - min_samples_split과 함께 과적합 제어 용도
  - 불균형 데이터의 경우 특정 클래스의 데이터가 극도로 작을 수 있으므로 작게 설정 필요
- max_features	- 최적의 분할을 위해 고려할 최대 feature 개수
  - Default = 'auto' (결정트리에서는 default가 none이었음)
  - int형으로 지정 →피처 갯수 / float형으로 지정 → 비중
  - sqrt 또는 auto : 전체 피처 중 √(피처개수) 만큼 선정
  - log : 전체 피처 중 log2(전체 피처 개수) 만큼 선정
- max_depth	- 트리의 최대 깊이
  - default = None → 완벽하게 클래스 값이 결정될 때 까지 분할 또는 데이터 개수가 min_samples_split보다 작아질 때까지 분할
  - 깊이가 깊어지면 과적합될 수 있으므로 적절히 제어 필요
- max_leaf_nodes	리프노드의 최대 개수
- learning_rate - 학습률
  - 0.0 ~ 1.0
  - 학습을 진행할 때마다 적용하는 학습률 

### 4. 랜덤포레스트_하이퍼파라미터_튜닝

### 5. GBM_하이퍼파라미터_튜닝_K겹검즘
- K겹 교차 검증(K-fold cross validation)
  - 데이터를 K개로 나누고 돌아가면서 훈련 데이터와 테스트 데이터로 나눠 검증을 진행하는 것입니다. 

### 6. LGBM
- LGBM, XGB, 결정트리, 보팅 다양한 기법을 사용해 보았습니다. 

### 7. 모델_생성_Keras
- Keras를 이용해 직접 신경망 모델을 구현해보았습니다. 
