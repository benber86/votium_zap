pragma solidity ^0.8.0;
// SPDX-License-Identifier: MIT

interface IMerkleStash {
    function claim(uint256 index, address account, uint256 amount, bytes32[] calldata merkleProof) external;
}