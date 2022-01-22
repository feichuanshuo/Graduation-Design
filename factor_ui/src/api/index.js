// 项目中所有的请求由这个文件发出
import axios from "axios";
import {BASIC_URL} from "../config";

// 获取供给、成交（拿地的数量和价格）
export const reqSupplyData = (len)=>axios.get(`${BASIC_URL}/supply_data?len=${len}`)
export const reqTransactionData = (len)=>axios.get(`${BASIC_URL}/transaction_data?len=${len}`)
