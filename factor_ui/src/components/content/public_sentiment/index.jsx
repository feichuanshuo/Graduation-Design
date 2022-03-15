import React, {Component} from 'react';
import {Card,Input,Row,Col,Tag,DatePicker} from "antd";
import 'moment/locale/zh-cn';
import locale from 'antd/es/date-picker/locale/zh_CN';
import {reqBaiduIndex} from "../../../api";
import "./index.less";

const { Search } = Input;
const { RangePicker } = DatePicker;

class PublicSentiment extends Component {

    baiduSearch = (value) => {
        reqBaiduIndex().then((res)=>{
            console.log(res)
        }).catch((err)=>{
            console.log(err)
        })
    }

    render() {
        return (
            <div>
                <Card
                    className="data-card"
                    title="百度指数"
                >
                    <Row
                        className="search-block"
                        gutter={10}
                    >
                        <Col span={8}>
                            <Search
                                placeholder="输入关键词探索以下吧！"
                                enterButton
                                onSearch={this.baiduSearch}
                            />
                            <Tag color="blue">限购</Tag>
                            <Tag color="magenta">土地供应</Tag>
                            <Tag color="green">房地产税</Tag>
                        </Col>
                        <Col>
                            <RangePicker
                                locale={locale}
                                allowClear
                            />
                        </Col>
                    </Row>
                </Card>
            </div>
        );
    }
}

export default PublicSentiment;
