import React, {Component} from 'react';
import {Card, Input, Row, Col, Tabs, DatePicker, message, Button} from "antd";
import 'moment/locale/zh-cn';
import locale from 'antd/es/date-picker/locale/zh_CN';
import {reqSentimentData} from "../../../api";
import { Line } from '@ant-design/plots';
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
        const config = {
            padding: 'auto',
            xField: 'month',
            yField: 'index',
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
            </Card>
        );
    }
}

export default PublicSentiment;
