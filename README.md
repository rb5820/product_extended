# Product Extended

## Overview
This module extends the standard Odoo product module with additional features for multi-company environments and manufacturer details.

## Features

### Multi-Company Support
- Associate products with multiple companies using the `allowed_company_ids` field
- Restrict products from specific companies using the `disallowed_company_ids` field
- Maintain proper visibility of products across a multi-company environment
- Security rules to enforce proper access control
- Validation to prevent a company from being both allowed and disallowed

### Manufacturer Details
- Track manufacturer information
  - Manufacturer partner
  - Manufacturer part numbers
  - Manufacturer model numbers
- Country of origin tracking
- Supplier information tracking

### Physical Specifications
- Weight in kilograms
- Dimensions tracking
  - Length (mm)
  - Width (mm)
  - Height (mm)
  - Computed dimensions field for easy display

### Inventory Tracking
- Support for serial number tracking on products
- Asset management for individual product units
- Warranty and service history tracking by serial number

### European Waste Codes
- Integration with the `product_waste_code` module
- Associate products with European Waste Classification (EWC) codes
- Track waste disposal requirements for regulatory compliance
- Proper waste management for end-of-life products

### IEC 62443 Security Capability Compliance
- Integration with the `mgmtsystem_iec62443_2023` module
- Track product compliance with IEC 62443 industrial security standards
- Security capability level assessment and visualization
- Compliance vector representation for the 7 Foundational Requirements (FR):
  - FR1: Identification & Authentication
  - FR2: Use Control
  - FR3: System Integrity
  - FR4: Data Confidentiality
  - FR5: Restricted Data Flow
  - FR6: Timely Response to Events
  - FR7: Resource Availability

## Configuration

### Multi-Company Setup
1. Go to Settings → Users & Companies → Companies
2. Create or configure your companies
3. Assign products to multiple companies through the product form

### Manufacturer Information
1. Navigate to the product form
2. Go to the "Manufacturing Details" tab
3. Enter manufacturer and supplier details
4. Add physical specifications

### IEC 62443 Security Configuration
1. Navigate to the product form
2. Go to the "IEC 62443 Capability Compliance" tab
3. Click "Configure Security Levels" to set compliance values
4. Generate assessment reports based on the compliance data

## Usage

### Filtering Products
- Filter products by manufacturer or supplier
- Group products by manufacturer, supplier, or country of origin
- In multi-company environments, filter by "Available in My Company"

### Searching Products
- Search by manufacturer details
- Find products by dimensions or weight
- Locate products by part numbers

## Technical Information

### Models Extended
- product.template: Added fields for manufacturer details and multi-company support

### New Fields
- manufacturer: Many2one relation to res.partner
- manufacturer_part_number: Char
- manufacturer_model_number: Char
- supplier: Many2one relation to res.partner
- supplier_article_number: Char
- supplier_model_number: Char
- country_of_origin: Many2one relation to res.country
- weight: Float (kg)
- length: Float (mm)
- width: Float (mm)
- height: Float (mm)
- dimensions: Char (computed field)
- allowed_company_ids: Many2many relation to res.company

## Demo Data
The module comes with demo data to showcase its functionality:

### Cisco Catalyst 9120AXE Wireless Access Point
A fully configured product example showing all extended features:
- Complete manufacturer details (Cisco Systems, Inc.)
- Supplier information (Network Solutions Provider)
- Physical dimensions (230 × 230 × 54 mm)
- Weight (1.25 kg)
- Multi-company settings (allowed/disallowed companies)
- Technical specifications including:
  - Wireless standards
  - Performance metrics
  - Connectivity options
  - Power requirements
  - Security features
  - Environmental specifications
  - Compliance certifications

### Meinberg LANTIME M320 GPS Network Time Server
A precision timing product example with:
- Complete manufacturer details (Meinberg Funkuhren GmbH & Co. KG)
- Supplier information (Time Systems Integrator GmbH)
- Physical dimensions (483 × 285 × 44 mm - standard 19" 1U rack mount)
- Weight (2.0 kg)
- Detailed technical specifications:
  - Network time server capabilities (NTP, SNTP, PTP)
  - GPS reference receiver specifications
  - Performance metrics and accuracy
  - Physical and environmental specifications
  - Compliance certifications

These demo products provide reference implementations you can use as templates for your own product configurations.

## License
LGPL-3
