import React, {Component} from 'react';
import {Card, DatePicker, message} from "antd";
import 'moment/locale/zh-cn';
import locale from 'antd/es/date-picker/locale/zh_CN';
import {reqSentimentData} from "../../../api";
import { DualAxes } from '@ant-design/plots';
import moment from 'moment';
import "./index.less";
import {getCurrentDate} from "../../../common/time";
import {SUCCESS_CODE} from "../../../config";

const { RangePicker } = DatePicker;

class PublicSentiment extends Component {

    state = {
        sentimentData:[],
        start_date: '2022-01-01',
        end_date: getCurrentDate(),
    }
    getSentiment = (search_word) => {
        const {start_date,end_date} = this.state;

        reqSentimentData(start_date,end_date).then((res)=>{
            const {code,msg,data} = res
            if (code === SUCCESS_CODE) {
                this.setState({
                    sentimentData:data
                })
            }
            else{
                message.warn(msg,1);
            }
        }).catch((err)=>{
            message.error('尚无此数据',1);
        })
    }

    componentDidMount() {
        this.getSentiment()
    }

    render() {
        const {sentimentData,start_date,end_date} = this.state;
        const priceData = sentimentData.map((item)=>{
            return {
                month:item.month,
                value:item.price,
                name:'西安市平均房价'
            }
        })
        const wordsData = []
        sentimentData.forEach((item)=>{
            wordsData.push({
                month:item.month,
                value:item.word_1,
                name:'热词:房价'
            })
            wordsData.push({
                month:item.month,
                value:item.word_2,
                name:'热词:房价上涨'
            })
            wordsData.push({
                month:item.month,
                value:item.word_3,
                name:'热词:房价下跌'
            })
            wordsData.push({
                month:item.month,
                value:item.word_4,
                name:'热词:房产税'
            })
            wordsData.push({
                month:item.month,
                value:item.word_5,
                name:'热词:房贷'
            })
        })
        const config = {
            data: [priceData, wordsData],
            xField: 'month',
            yField: ['value', 'value'],
            geometryOptions: [
                {
                    geometry: 'line',
                    seriesField: 'name',
                    lineStyle: {
                        lineWidth: 3,
                        lineDash: [5, 5],
                    },
                    smooth: true,
                },
                {
                    geometry: 'line',
                    seriesField: 'name',
                    point: {},
                },
            ],
        };

        return (
            <Card
                className="data-card"
                title="舆情与房价"
                extra={
                    <RangePicker
                        picker="month"
                        locale={locale}
                        allowClear
                        value={[
                            start_date?moment(start_date):null,
                            end_date?moment(end_date):null,
                        ]}
                        onChange = {(value)=>{
                            this.setState({
                                start_date: value[0].format('YYYY-MM-DD'),
                                end_date: value[1].format('YYYY-MM-DD')
                            })
                        }}
                        onBlur={this.getSentiment}
                        disabledDate={(date)=>{
                            const current = new Date().getTime()
                            return current - date['_d'].getTime() < 0
                        }}
                    />
                }
            >
                <DualAxes {...config} />
            </Card>
        );
    }
}

export default PublicSentiment;
