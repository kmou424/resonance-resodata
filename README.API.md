## GET /api/fetch/goods_info

此接口为通用数据获取接口。

##### 请求参数

| 参数名  | 类型   | 位置  | 描述                                   | 是否必需 |
| ------- | ------ | ----- | -------------------------------------- | -------- |
| station | string | query | 筛选条件 站点名（中文，如“7号自由港”） | 否       |
| good    | string | query | 筛选条件 商品名（中文，如“发动机”）    | 否       |

##### 返回参数

| 参数名             | 类型   | 描述                                       |
| ------------------ | ------ | ------------------------------------------ |
| [object]           | array  | 商品信息数组                               |
| > name             | string | 商品名（中文，如“发动机”）                 |
| > station          | string | 站点名（中文，如“7号自由港”）              |
| > price            | number | 当前价格                                   |
| > next_trend       | number | 下次价格变化趋势（> 0 则上涨，< 0 则下降） |
| > update_time      | string | 更新时间（UTC +0; yyyy-MM-dd HH:mm:ss）    |
| > update_timestamp | number | 更新时间（UTC +0; Unix时间戳）             |

## GET /api/fetch/full_goods_info

此接口仅供比对数据为本项目做贡献使用。

##### 请求参数

| 参数名  | 类型   | 位置  | 描述                                                         | 是否必需 |
| ------- | ------ | ----- | ------------------------------------------------------------ | -------- |
| station | string | query | 站点名（中文，如“7号自由港”）                                | 是       |
| show    | string | query | 筛选（不指定则默认full，显示所有数据；可选unknown，仅显示未记录在映射表里的数据） | 否       |

##### 返回参数

| 参数名             | 类型   | 描述                                                    |
| ------------------ | ------ | ------------------------------------------------------- |
| [object]           | array  | 商品信息数组                                            |
| > id               | string | 商品编号，仅作数据维护使用                              |
| > name             | string | 商品名（中文，如“发动机”，未记录数据则显示为“Unknown”） |
| > station          | string | 站点名（中文，与传入station保持一致）                   |
| > price            | number | 当前价格                                                |
| > next_trend       | number | 下次价格变化趋势（> 0 则上涨，< 0 则下降）              |
| > update_time      | string | 更新时间（UTC +0; yyyy-MM-dd HH:mm:ss）                 |
| > update_timestamp | number | 更新时间（UTC +0; Unix时间戳）                          |

