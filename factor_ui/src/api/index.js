// 项目中所有的请求由这个文件发出
import axios from "./myAxios";
import {BASIC_URL} from "../config";

// 获取供给、成交（拿地的数量和价格）
export const reqSupplyData = (len)=>axios.get(`${BASIC_URL}/supply_data?len=${len}`)
export const reqTransactionData = (len)=>axios.get(`${BASIC_URL}/transaction_data?len=${len}`)

// 获取人口信息
export const reqPopulationData = (len)=>axios.get(`${BASIC_URL}/population_data?len=${len}`)

// 获取百度指数
export const reqBaiduIndex = (word,start_date,end_date)=>axios.get(`${BASIC_URL}/public_sentiment/baidu_index?word=${word}&start_date=${start_date}&end_date=${end_date}`)

// 获取小区详情
export const reqDetailData = (name)=>axios.get(`${BASIC_URL}/detail/detail_data?name=${name}`)

// 获取包含指定关键字的小区列表
export const reqSearchHint = (keyword)=>axios.get(`${BASIC_URL}/detail/search_hint?keyword=${keyword}`)
