import React, { useState } from 'react';
import { AgGridReact, AgGridColumn } from 'ag-grid-react';
import 'ag-grid-community/dist/styles/ag-grid.css';
import "ag-grid-community/dist/styles/ag-theme-alpine.css";

const BhavTable = (props) => {
  const [gridApi, setGridApi] = useState(null);
  const [gridColumnApi, setGridColumnApi] = useState(null);

  const onGridReady = (params) => {
    setGridApi(params.api);
    setGridColumnApi(params.columnApi);
  };


  return (
    <div style={{
      width: '100%',
      height: '500px'
    }}>
      <div style={{ height: '100%', boxSizing: 'border-box' }}>
        <div
          id="myGrid"
          style={{
            height: '100%',
            width: '100%',
          }}
          className="ag-theme-alpine"
        >
          <AgGridReact
            rowSelection={'multiple'}
            rowMultiSelectWithClick={true}
            rowData={props.data}
            onGridReady={onGridReady}
          >
            <AgGridColumn
              headerName="SC_NAME"
              field="SC_NAME"
              sortable={true}
            />

            <AgGridColumn
              sortable={true}
              headerName="SC_CODE"
              field="SC_CODE"
            />
            <AgGridColumn
              headerName="OPEN"
              field="OPEN"
              sortable={true}
            />
            <AgGridColumn
              headerName="HIGH"
              field="HIGH"
              sortable={true}
            />
            <AgGridColumn
              headerName="LOW"
              field="LOW"
              sortable={true}

            />
            <AgGridColumn
              headerName="CLOSE"
              field="CLOSE"
              sortable={true}
            />
            <AgGridColumn
              headerName="DAY"
              field="DAY"
              sortable={true}
            />
            <AgGridColumn
              headerName="MONTH"
              field="MONTH"
              sortable={true}
            />

            <AgGridColumn
              headerName="YEAR"
              field="YEAR"
              sortable={true}
            />
          </AgGridReact>
        </div>
      </div>
    </div>
  );
};

export default BhavTable;