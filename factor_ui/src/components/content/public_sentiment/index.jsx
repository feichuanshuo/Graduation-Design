import React, {Component} from 'react';
import {Card, Input, Row, Col, Tabs, DatePicker, message} from "antd";
import 'moment/locale/zh-cn';
import locale from 'antd/es/date-picker/locale/zh_CN';
import {reqBaiduIndex} from "../../../api";
import { Line } from '@ant-design/plots';
import moment from 'moment';
import "./index.less";
import {getCurrentDate} from "../../../common/time";
import {SUCCESS_CODE} from "../../../config";

const { Search } = Input;
const { RangePicker } = DatePicker;
const { TabPane } = Tabs;

class PublicSentiment extends Component {

    state = {
        search_word: '房产税',
        baidu_index: {
            search_index: [],
            info_index: [],
            media_index: [],
        },
        baidu_index_date: {
            start_date: '2022-01-01',
            end_date: getCurrentDate(),
        },
    }
    getBaiduIndex = (search_word) => {
        const {start_date,end_date} = this.state.baidu_index_date;

        if (!(search_word&&start_date&&end_date)) {
            message.warn('请输入时间和关键词',1);
        }
        reqBaiduIndex(search_word,start_date,end_date).then((res)=>{
            if (res.code === SUCCESS_CODE) {
                this.setState({
                    search_word,
                    baidu_index: res.data,
                })
            }
            else{
                message.warn(res.msg,1);
            }
        }).catch((err)=>{
            message.error('尚无此数据',1);
        })
    }


    componentDidMount() {
        this.getBaiduIndex('房产税');
    }

    render() {
        const {baidu_index,search_word} = this.state;
        const config_baidu = {
            padding: 'auto',
            xField: 'Date',
            yField: 'index',
        };

        return (
            <Card
                className="data-card"
                title="百度指数"
                extra={
                    <Row
                        className="search-block"
                        gutter={10}
                    >
                        <Col>
                            <RangePicker
                                locale={locale}
                                allowClear
                                value={[
                                    this.state.baidu_index_date.start_date?moment(this.state.baidu_index_date.start_date):null,
                                    this.state.baidu_index_date.end_date?moment(this.state.baidu_index_date.end_date):null,
                                ]}
                                onChange={(value)=>{
                                    this.setState({
                                        baidu_index_date: {
                                            start_date: value[0].format('YYYY-MM-DD'),
                                            end_date: value[1].format('YYYY-MM-DD')
                                        }
                                    })
                                }}
                                disabledDate={(date)=>{
                                    const current = new Date().getTime()
                                    return current - date['_d'].getTime() < 0
                                }}
                            />
                        </Col>
                        <Col>
                            <Search
                                placeholder="输入关键词探索以下吧！"
                                enterButton
                                onSearch={this.getBaiduIndex}
                            />
                        </Col>
                    </Row>
                }
            >
                <Tabs
                    defaultActiveKey="1"
                    tabPosition="left"
                >
                    <TabPane tab="搜索指数" key="1">
                        <div className={"search-word"}>{search_word}</div>
                        <Line {...config_baidu} data={baidu_index.search_index}/>
                    </TabPane>
                    <TabPane tab="资讯指数" key="2">
                        <div className={"search-word"}>{search_word}</div>
                        <Line {...config_baidu} data={baidu_index.info_index}/>
                    </TabPane>
                    <TabPane tab="媒体指数" key="3">
                        <div className={"search-word"}>{search_word}</div>
                        <Line {...config_baidu} data={baidu_index.media_index}/>
                    </TabPane>
                </Tabs>
            </Card>
        );
    }
}

export default PublicSentiment;
