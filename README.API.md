## GET /api/fetch/goods_info

此接口为通用数据获取接口。

##### 请求参数

| 参数名  | 类型   | 位置  | 描述                                   | 是否必需 |
| ------- | ------ | ----- | -------------------------------------- | -------- |
| station | string | query | 筛选条件 站点名（中文，如“7号自由港”） | 否       |
| good    | string | query | 筛选条件 商品名（中文，如“发动机”）    | 否       |
| uuid    | string | query | 鉴权 UUID                              | 是       |

##### 返回参数

| 参数名             | 类型   | 描述                                       |
| ------------------ | ------ | ------------------------------------------ |
| [object]           | array  | 商品信息数组                               |
| > name             | string | 商品名（中文，如“发动机”）                 |
| > station          | string | 站点名（中文，如“7号自由港”）              |
| > stock            | number | 基础货量                                   |
| > type             | string | 交易类型（buy为站点收购，sell为站点出售）  |
| > base_price       | number | 基础价格                                   |
| > price            | number | 当前价格                                   |
| > next_trend       | number | 下次价格变化趋势（> 0 则上涨，< 0 则下降） |
| > update_time      | string | 更新时间（UTC +0; yyyy-MM-dd HH:mm:ss）    |
| > update_timestamp | number | 更新时间（UTC +0; Unix时间戳）             |
